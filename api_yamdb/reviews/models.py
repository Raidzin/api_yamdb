from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    """
    Категории произведений.

    Поля: id, name, slug, titles.
    """
    name = models.TextField(
        verbose_name='Название',
        max_length=150
    )
    slug = models.SlugField(
        verbose_name='идентификатор'
    )

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Жанры.

    Поля: id, name, slug, titles.
    """
    name = models.TextField(
        verbose_name='Название',
        max_length=150,
    )
    slug = models.SlugField(
        verbose_name='идентификатор'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Title(models.Model):
    """
    Произведения.

    Поля: id, name, year, category, genres.
    """
    name = models.TextField(
        verbose_name='Название',
        max_length=150,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    year = models.IntegerField(
        verbose_name='Год',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='titles'
    )

    @property
    def rating(self):
        return Review.objects.filter(
            id=self.id
        ).aggregate(models.Avg('score'))['score__avg']

    class Meta:
        ordering = '-year',
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
