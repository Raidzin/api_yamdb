from django.db import models


class Categories(models.Model):
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


class Titles(models.Model):
    """
    Произведения.

    Поля: id, name, year, category, genres.
    """
    name = models.TextField(
        verbose_name='Название',
        max_length=150,
    )
    year = models.IntegerField(
        verbose_name='Год',
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )

    class Meta:
        ordering = '-year',
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Genres(models.Model):
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
    titles = models.ManyToManyField(
        Titles,
        related_name='genres',
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


