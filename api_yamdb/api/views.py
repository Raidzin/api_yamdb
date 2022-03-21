from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from rest_framework import filters, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api_yamdb.settings import DEFAULT_FROM_EMAIL
from reviews.models import User, Title, Category, Genre, Review
from .filters import TitleFilter
from .permissions import (
    IsAdmin,
    ReadOnlyOrAdmin,
    CreateOrModeratorDeleteOrAdmin
)
from .serializers import (
    ForAdminSerializer, UserSerializerOrReadOnly,
    SignupSerializer, TokenSerializer,
    OutputTitleSerializer, InputTitleSerializer,
    CategorySerializer, GenreSerializer,
    ReviewSerializer, CommentSerializer,
)

CONFIRMATION_CODE = 'Код подтверждения для завершения регистрации'
MESSAGE_FOR_YOUR_CONFIRMATION_CODE = 'Ваш код для получения JWT токена'


class APISignUp(APIView):
    """Регистрация пользователя."""
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        username = serializer.validated_data.get('username')
        user_by_email = User.objects.filter(
            email=serializer.validated_data['email']).exists()
        user_by_username = User.objects.filter(
            username=serializer.validated_data['username']).exists()
        not_valid = user_by_email != user_by_username
        if not User.objects.filter(
            username=username,
            email=email
        ).exists():
            if user_by_email and not_valid:
                raise ValidationError('Почта занята')
            if user_by_username and not_valid:
                raise ValidationError('Имя занято')
            User.objects.create(
                username=username,
                email=email
            )
        user = User.objects.get(username=username,
                                email=email)
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            CONFIRMATION_CODE,
            f'{MESSAGE_FOR_YOUR_CONFIRMATION_CODE} {confirmation_code}',
            DEFAULT_FROM_EMAIL,
            [request.data['email']],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class APIToken(APIView):
    """Выдача токена"""
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        confirmation_code = serializer.validated_data['confirmation_code']
        user = get_object_or_404(User, username=username)

        if (user and default_token_generator.check_token(
                user, confirmation_code)):
            user.is_active = True
            user.save()
        else:
            response = {
                'confirmation_code': 'Токен не валидный'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken.for_user(user)
        response = {
            'token': str(token.access_token),
        }
        return Response(response, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    """API для работы пользователями"""

    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = ForAdminSerializer
    permission_classes = (IsAdmin,)
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('username',)

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        """
        Запрос и возможность редактирования
        информации профиля пользователя.
        """
        user = get_object_or_404(User, username=request.user.username)
        if request.method == 'GET':
            serializer = UserSerializerOrReadOnly(user, many=False)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = UserSerializerOrReadOnly(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class TitleInfoViewSet(viewsets.ModelViewSet):
    permission_classes = ReadOnlyOrAdmin,
    pagination_class = PageNumberPagination
    filter_backends = filters.SearchFilter,
    search_fields = 'name',

    def destroy(self, *args, **kwargs):
        get_object_or_404(
            self.get_queryset(),
            slug=kwargs.get('slug')
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(TitleInfoViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GenreViewSet(TitleInfoViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = ReadOnlyOrAdmin,
    pagination_class = PageNumberPagination
    filter_backends = TitleFilter,
    filter_fields = 'genre__slug', 'category__slug', 'year', 'name'

    def get_queryset(self):
        return Title.objects.annotate(rating=Avg('reviews__score'))

    def get_serializer_class(self):
        if self.request._request.method in SAFE_METHODS:
            return OutputTitleSerializer
        return InputTitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = CreateOrModeratorDeleteOrAdmin,

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = CreateOrModeratorDeleteOrAdmin,

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)
