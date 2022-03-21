from django.shortcuts import get_object_or_404
from reviews.models import Title
from rest_framework.exceptions import ValidationError
from django.core.validators import validate_email
from reviews.models import User

RESERVED_NAME = 'me'
RESERVED_NAME_ERROR = 'Имя пользователя "me" использовать нельзя.'
USER_OR_NAME_REGISTERED = 'Пользователь с таким именем уже зарегестрирован.'
USER_OR_EMAIL_REGISTERED = 'Пользователь с такой почтой уже зарегестрирован.'


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
        validate_email(email)
    except ValidationError:
        raise ValidationError(
            {'email': 'Введите корректный email.'}
        )
