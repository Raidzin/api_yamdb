from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Category, Comment, Genre, Review, Title, User

from .utils import CurrentTitleDefault, email_validate, validate_username


SCORE_ERROR = 'Оценка может быть от 1 до 10!'
OCCUPIED_USERNAME_ERROR = "Имя пользователя '{}' уже занято"
USERNAME_RE = '^[A-Za-z0-9@.+-_]+$'


class TokenSerializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=USERNAME_RE, max_length=150, required=True,
        validators=[validate_username]
    )
    confirmation_code = serializers.CharField(
        required=True,
    )


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[email_validate]
    )
    username = serializers.CharField(
        required=True, validators=[validate_username]
    )


class ForAdminSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[validate_username])

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': OCCUPIED_USERNAME_ERROR.format(username)})
        return username


class UserSerializerOrReadOnly(ForAdminSerializer):
    username = serializers.CharField(validators=[validate_username])

    class Meta(ForAdminSerializer.Meta):
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class InputTitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Title
        fields = 'id', 'name', 'year', 'description', 'genre', 'category'


class OutputTitleSerializer(InputTitleSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField()

    class Meta(InputTitleSerializer.Meta):
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')
        read_only_fields = '__all__',


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username'
    )
    title = serializers.HiddenField(
        default=CurrentTitleDefault()
    )

    score = serializers.IntegerField(
        validators=[MaxValueValidator(10, SCORE_ERROR),
                    MinValueValidator(1, SCORE_ERROR)]
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
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment
