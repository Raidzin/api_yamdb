from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User

from reviews.models import (
    Title,
    Review,
    Category,
    Genre
)
from .permissions import (IsAdmin, IsAuthorOrAdministratorOrReadOnly)
from .serializers import (ForAdminSerializer,
                          TokenSerializer,
                          UserSerializerOrReadOnly, ReviewSerializer,
                          CommentSerializer, TitleSerializer,
                          CategorySerializer, GenreSerializer,
                          )
from .utils import generate_and_send_confirmation_code_to_email


class APISignUp(APIView):
    """Регистрация пользователя."""
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializerOrReadOnly(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            generate_and_send_confirmation_code_to_email(
                serializer.data['username'])
            return Response(
                {'email': serializer.data['email'],
                 'username': serializer.data['username']},
                status=status.HTTP_200_OK)


class APIToken(APIView):
    """Выдача токена"""
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = get_object_or_404(
                User, username=serializer.data['username'])
            if default_token_generator.check_token(
                    user, serializer.data['confirmation_code']):
                token = AccessToken.for_user(user)
                return Response(
                    {'token': str(token)}, status=status.HTTP_200_OK)
            return Response({
                'confirmation code': 'Некорректный код подтверждения!'},
                status=status.HTTP_400_BAD_REQUEST)


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
                partial=True, many=False
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = IsAuthorOrAdministratorOrReadOnly,
    queryset = Title.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = IsAuthorOrAdministratorOrReadOnly,
    queryset = Category.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    permission_classes = IsAuthorOrAdministratorOrReadOnly,
    queryset = Genre.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = IsAuthorOrAdministratorOrReadOnly,

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
    permission_classes = IsAuthorOrAdministratorOrReadOnly,

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)
