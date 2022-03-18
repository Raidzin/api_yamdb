import uuid

from api_yamdb.settings import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from reviews.models import Title, User

CONFIRMATION_CODE = 'Код подтвержения для завершения регистрации'
MESSAGE_FOR_YOUR_CONFIRMATION_CODE = 'Ваш код для получения JWT токена'


class CurrentTitleDefault:
    requires_context = True

    def __call__(self, serializer_field):
        title_id = serializer_field.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title

    def __repr__(self):
        return '%s()' % self.__class__.__name__


def generate_and_send_confirmation_code_to_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = str(uuid.uuid3(uuid.NAMESPACE_DNS, username))
    user.confirmation_code = confirmation_code
    send_mail(
        CONFIRMATION_CODE,
        f'{MESSAGE_FOR_YOUR_CONFIRMATION_CODE} {user.confirmation_code}',
        DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
    user.save()
