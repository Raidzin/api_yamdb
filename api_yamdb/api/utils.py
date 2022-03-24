from django.core.validators import validate_email
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from reviews.models import Title, User

RESERVED_NAME = 'me'
RESERVED_NAME_ERROR = 'Имя пользователя "me" использовать нельзя.'
USER_OR_NAME_REGISTERED = 'Пользователь с таким именем уже зарегестрирован.'
USER_OR_EMAIL_REGISTERED = 'Пользователь с такой почтой уже зарегестрирован.'
INVALID_EMAIL = 'Введите корректный email.'


class CurrentTitleDefault:
    requires_context = True

    def __call__(self, serializer_field):
        title_id = serializer_field.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title

    def __repr__(self):
        return '%s()' % self.__class__.__name__


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
