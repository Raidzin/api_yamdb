from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from reviews.models import Comment, Review, Title, Category, Genre
from users.models import User

from .utils import CurrentTitleDefault

RESERVED_NAME = 'me'
RESERVED_NAME_ERROR = 'Имя пользователя "me" использовать нельзя.'
USER_NOT_FOUND_ERROR = 'Пользователя с таким именем не существует.'
SCORE_ERROR = 'Оценка может быть от 1 до 10!'


class TokenSerializer(serializers.Serializer):
    """Сериализатор для получения токена."""
    username = serializers.CharField(max_length=200, required=True)
    confirmation_code = serializers.CharField(max_length=200, required=True)

    def validate_username(self, value):
        """Зарезервированное имя использовать нельзя."""
        if value == RESERVED_NAME:
            raise serializers.ValidationError(RESERVED_NAME_ERROR)
        if not User.objects.filter(username=value).exists():
            raise exceptions.NotFound(USER_NOT_FOUND_ERROR)
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
            raise serializers.ValidationError(RESERVED_NAME_ERROR)
        return value


class UserSerializerOrReadOnly(ForAdminSerializer):
    """Сериалайзер пользователей(чтение)"""

    class Meta(ForAdminSerializer.Meta):
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий произведений."""

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор жанров произведений."""

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class BaseTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = 'id', 'name', 'year', 'description', 'genre', 'category'


class InputTitleSerializer(BaseTitleSerializer):
    """Сериализатор произведений для получения данных."""
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )


class OutputTitleSerializer(BaseTitleSerializer):
    """Сериализатор произведений для отправки данных."""
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField()

    class Meta(BaseTitleSerializer.Meta):
        fields = 'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        read_only_fields = '__all__',


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзывов."""
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username'
    )
    title = serializers.HiddenField(
        default=CurrentTitleDefault())

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date', 'title')
        model = Review
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('author', 'title')
            )
        ]

    def validate(self, data):
        if not 1 <= data['score'] <= 10:
            raise serializers.ValidationError(SCORE_ERROR)
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment
