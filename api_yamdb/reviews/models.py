from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

FUTURE_ERROR = 'Нельзя сохранять анонсированные произведения'


class User(AbstractUser):
    """Добавление дополнительных полей."""
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLES = (
        (ADMIN, ADMIN),
        (MODERATOR, MODERATOR),
        (USER, USER)
    )
    role = models.CharField(
        max_length=200,
        choices=ROLES,
        default=USER
    )
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=150, unique=True, db_index=True)
    confirmation_code = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.is_staff or self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER


class Category(models.Model):
    name = models.TextField(
        verbose_name='Название',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='идентификатор',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField(
        verbose_name='Название',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='идентификатор',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(
        verbose_name='Название',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
    )
    year = models.IntegerField(
        verbose_name='Год',
        validators=(
            MaxValueValidator(
                datetime.now().year,
                FUTURE_ERROR
            ),
        ),
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles'
    )

    class Meta:
        ordering = '-year', 'name'
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField(
        verbose_name='Текст отзыва'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.IntegerField(
        validators=[
            MaxValueValidator(10, 'Максимальная оценка - 10'),
            MinValueValidator(1, 'Минимальная оценка - 1')
        ],
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_review'
            )
        ]

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField(
        verbose_name='Комментарий'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = "Комментарий к отзыву"
        verbose_name_plural = "Комментарии к отзыву"

    def __str__(self):
        return self.text[:15]
