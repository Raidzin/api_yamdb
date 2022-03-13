from django.db import models
from django.contrib.auth.models import AbstractUser


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
        max_length=20,
        choices=ROLES,
        default=USER
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(
        blank=True
    )
    username = models.CharField(max_length=150, unique=True, db_index=True)

    confirmation_code = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ('role',)

    @property
    def is_admin(self):
        return self.is_staff or self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
