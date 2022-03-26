```
 ______  ____    ______      __    __                 ____    __        
/\  _  \/\  _`\ /\__  _\    /\ \  /\ \        /'\_/`\/\  _`\ /\ \       
\ \ \L\ \ \ \L\ \/_/\ \/    \ `\`\\/'/  __   /\      \ \ \/\ \ \ \____  
 \ \  __ \ \ ,__/  \ \ \     `\ `\ /' /'__`\ \ \ \__\ \ \ \ \ \ \ '__`\ 
  \ \ \/\ \ \ \/    \_\ \__    `\ \ \/\ \L\.\_\ \ \_/\ \ \ \_\ \ \ \L\ \
   \ \_\ \_\ \_\    /\_____\     \ \_\ \__/.\_\\ \_\\ \_\ \____/\ \_,__/
    \/_/\/_/\/_/    \/_____/      \/_/\/__/\/_/ \/_/ \/_/\/___/  \/___/ 

```
                                                                        
  
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). 
Произведения делятся на категории:

- "Книги"
- "Фильмы"
- "Музыка"

Список категорий (Category) может быть расширен администратором (например, можно добавить категорию "Ювелирка"). Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв. Подробная документация доступна по адресу http://127.0.0.1:8000/redoc/ после запуска проекта. Процедура запуска проекта представлена ниже.

## Техническое описание
Пользовательские роли
- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
- Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django — обладает правами администратора (admin).

Алгоритм регистрации пользователей
Для добавления нового пользователя нужно отправить POST-запрос с параметрами email и username на эндпоинт /api/v1/auth/signup/. Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен). В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом. После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт /api/v1/users/me/ и заполнить поля в своём профайле (описание полей — в документации). Если пользователя создаёт администратор, например, через POST-запрос на эндпоинт api/v1/users/ — письмо с кодом отправлять не нужно (описание полей запроса для этого случая — в документации).

## Технологии в проекте
- Python 3.7.9
- Django Framework
- Django Rest Framework
- Django Rest Framework Simplejwt
## Процедура запуска проекта
Клонировать репозиторий и перейти в него в командной строке

`git clone https://github.com/Raidzin/api_yamdb cd api_yamdb`

Cоздать и активировать виртуальное окружение

`python3 -m venv venv source venv/Scripts/activate`

Обновить pip и установить зависимости из файла requirements.txt

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Перейти в директорию api_yamdb

`cd api_yamdb`

Выполнить миграции

`python manage.py migrate`

Создать суперпользователя

`python manage.py createsuperuser`

Запустить проект

`python manage.py runserver`

Открыть документацию можно по ссылке

http://127.0.0.1:8000/redoc/

Загрузить данные из csv можно с помощью скрипта

`cd api_yamdb`

`python write_data.py`

### Авторы проекта:
- [Алексей Гончарук](https://github.com/Raidzin "Github")
- [Валерия Егорова](https://github.com/Valeria7317 "Github")
- [Дмитрий Осипов](https://github.com/chin0318 "Github")
