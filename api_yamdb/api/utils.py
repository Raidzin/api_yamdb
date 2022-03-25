from django.core.validators import validate_email
from rest_framework.exceptions import ValidationError
from reviews.models import User

RESERVED_NAME = 'me'
RESERVED_NAME_ERROR = 'Имя пользователя "me" использовать нельзя.'
USER_OR_NAME_REGISTERED = 'Пользователь с таким именем уже зарегестрирован.'
USER_OR_EMAIL_REGISTERED = 'Пользователь с такой почтой уже зарегестрирован.'
INVALID_EMAIL = 'Введите корректный email.'


def validate_username(value):
    if value == RESERVED_NAME:
        raise ValidationError(RESERVED_NAME_ERROR)
    return value


def email_validate(email):
    try:
        if not User.objects.filter(email=email).exists():
            validate_email(email)
    except ValidationError:
        raise ValidationError(
            {'email': INVALID_EMAIL}
        )
