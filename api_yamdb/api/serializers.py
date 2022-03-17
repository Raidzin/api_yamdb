from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from reviews.models import Comment, Review
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils import CurrentTitleDefault

RESERVED_NAME = 'me'
MESSAGE_FOR_RESERVED_NAME = 'Имя пользователя "me" использовать нельзя.'
MESSAGE_FOR_USER_NOT_FOUND = 'Пользователя с таким именем не существует.'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username'
    )
    title = serializers.HiddenField(
        default=CurrentTitleDefault())

    score = serializers.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date', 'title')
        model = Review
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('author', 'title')
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment


class UserSerializerOrReadOnly(serializers.ModelSerializer):
    """Сериалайзер пользователей(чтение)"""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('role', )

    def validate_username(self, value):
        """Зарезервированное имя использовать нельзя."""
        if value == RESERVED_NAME:
            raise serializers.ValidationError(MESSAGE_FOR_RESERVED_NAME)
        return value


class ForAdminSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей со статусом admin."""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')

    def validate_username(self, value):
        if value == RESERVED_NAME:
            raise serializers.ValidationError(MESSAGE_FOR_RESERVED_NAME)
        return value


class TokenSerializer(serializers.Serializer):
    """Сериализатор для получения токена."""
    username = serializers.CharField(max_length=200, required=True)
    confirmation_code = serializers.CharField(max_length=200, required=True)

    def validate_username(self, value):
        """Зарезервированное имя использовать нельзя."""
        if value == RESERVED_NAME:
            raise serializers.ValidationError(MESSAGE_FOR_RESERVED_NAME)
        if not User.objects.filter(username=value).exists():
            raise exceptions.NotFound(MESSAGE_FOR_USER_NOT_FOUND)
        return value
