BEGIN TRANSACTION;
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2022-03-20 08:28:06.220658');
INSERT INTO "django_migrations" VALUES (2,'contenttypes','0002_remove_content_type_name','2022-03-20 08:28:06.346535');
INSERT INTO "django_migrations" VALUES (3,'auth','0001_initial','2022-03-20 08:28:06.550544');
INSERT INTO "django_migrations" VALUES (4,'auth','0002_alter_permission_name_max_length','2022-03-20 08:28:06.691123');
INSERT INTO "django_migrations" VALUES (5,'auth','0003_alter_user_email_max_length','2022-03-20 08:28:06.848270');
INSERT INTO "django_migrations" VALUES (6,'auth','0004_alter_user_username_opts','2022-03-20 08:28:06.973704');
INSERT INTO "django_migrations" VALUES (7,'auth','0005_alter_user_last_login_null','2022-03-20 08:28:07.067886');
INSERT INTO "django_migrations" VALUES (8,'auth','0006_require_contenttypes_0002','2022-03-20 08:28:07.177760');
INSERT INTO "django_migrations" VALUES (9,'auth','0007_alter_validators_add_error_messages','2022-03-20 08:28:07.256244');
INSERT INTO "django_migrations" VALUES (10,'auth','0008_alter_user_username_max_length','2022-03-20 08:28:07.381646');
INSERT INTO "django_migrations" VALUES (11,'auth','0009_alter_user_last_name_max_length','2022-03-20 08:28:07.507044');
INSERT INTO "django_migrations" VALUES (12,'auth','0010_alter_group_name_max_length','2022-03-20 08:28:07.616896');
INSERT INTO "django_migrations" VALUES (13,'auth','0011_update_proxy_permissions','2022-03-20 08:28:07.746858');
INSERT INTO "django_migrations" VALUES (14,'reviews','0001_initial','2022-03-20 08:28:07.915072');
INSERT INTO "django_migrations" VALUES (15,'admin','0001_initial','2022-03-20 08:28:08.072146');
INSERT INTO "django_migrations" VALUES (16,'admin','0002_logentry_remove_auto_add','2022-03-20 08:28:08.307441');
INSERT INTO "django_migrations" VALUES (17,'admin','0003_logentry_add_action_flag_choices','2022-03-20 08:28:08.526600');
INSERT INTO "django_migrations" VALUES (18,'sessions','0001_initial','2022-03-20 08:28:08.714979');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (5,'sessions','session');
INSERT INTO "django_content_type" VALUES (6,'reviews','user');
INSERT INTO "django_content_type" VALUES (7,'reviews','category');
INSERT INTO "django_content_type" VALUES (8,'reviews','genre');
INSERT INTO "django_content_type" VALUES (9,'reviews','title');
INSERT INTO "django_content_type" VALUES (10,'reviews','review');
INSERT INTO "django_content_type" VALUES (11,'reviews','comment');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (14,4,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (15,4,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (16,4,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (17,5,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (18,5,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (19,5,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (20,5,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (21,6,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (22,6,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (23,6,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (24,6,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (25,7,'add_category','Can add Категорию');
INSERT INTO "auth_permission" VALUES (26,7,'change_category','Can change Категорию');
INSERT INTO "auth_permission" VALUES (27,7,'delete_category','Can delete Категорию');
INSERT INTO "auth_permission" VALUES (28,7,'view_category','Can view Категорию');
INSERT INTO "auth_permission" VALUES (29,8,'add_genre','Can add Жанр');
INSERT INTO "auth_permission" VALUES (30,8,'change_genre','Can change Жанр');
INSERT INTO "auth_permission" VALUES (31,8,'delete_genre','Can delete Жанр');
INSERT INTO "auth_permission" VALUES (32,8,'view_genre','Can view Жанр');
INSERT INTO "auth_permission" VALUES (33,9,'add_title','Can add Произведение');
INSERT INTO "auth_permission" VALUES (34,9,'change_title','Can change Произведение');
INSERT INTO "auth_permission" VALUES (35,9,'delete_title','Can delete Произведение');
INSERT INTO "auth_permission" VALUES (36,9,'view_title','Can view Произведение');
INSERT INTO "auth_permission" VALUES (37,10,'add_review','Can add Отзыв');
INSERT INTO "auth_permission" VALUES (38,10,'change_review','Can change Отзыв');
INSERT INTO "auth_permission" VALUES (39,10,'delete_review','Can delete Отзыв');
INSERT INTO "auth_permission" VALUES (40,10,'view_review','Can view Отзыв');
INSERT INTO "auth_permission" VALUES (41,11,'add_comment','Can add Комментарий к отзыву');
INSERT INTO "auth_permission" VALUES (42,11,'change_comment','Can change Комментарий к отзыву');
INSERT INTO "auth_permission" VALUES (43,11,'delete_comment','Can delete Комментарий к отзыву');
INSERT INTO "auth_permission" VALUES (44,11,'view_comment','Can view Комментарий к отзыву');
INSERT INTO "reviews_user" VALUES (1,'pbkdf2_sha256$150000$KVNwJhkFGRhG$QyCD4vk7bU5mmv6X7Vp9lY6a4BmGGejpn7bB/voWTA8=','2022-03-03 12:37:15.556608',1,'','',1,1,'2022-03-03 12:25:09.646055','user','ad@da.ew','','alex','');
INSERT INTO "reviews_user" VALUES (100,'','',0,'','',0,1,'2022-03-03 12:25:09.646055','user','bingobongo@yamdb.fake','','bingobongo','');
INSERT INTO "reviews_user" VALUES (101,'','',0,'','',0,1,'2022-03-03 12:25:09.646056','admin','capt_obvious@yamdb.fake','','capt_obvious','');
INSERT INTO "reviews_user" VALUES (102,'','',0,'','',0,1,'2022-03-03 12:25:09.646057','user','faust@yamdb.fake','','faust','');
INSERT INTO "reviews_user" VALUES (103,'','',0,'','',0,1,'2022-03-03 12:25:09.646058','user','reviewer@yamdb.fake','','reviewer','');
INSERT INTO "reviews_user" VALUES (104,'','',0,'','',0,1,'2022-03-03 12:25:09.646059','moderator','angry@yamdb.fake','','angry','');
INSERT INTO "reviews_category" VALUES (1,'movie','Фильм');
INSERT INTO "reviews_category" VALUES (2,'book','Книга');
INSERT INTO "reviews_category" VALUES (3,'music','Музыка');
INSERT INTO "reviews_genre" VALUES (1,'drama','Драма');
INSERT INTO "reviews_genre" VALUES (2,'comedy','Комедия');
INSERT INTO "reviews_genre" VALUES (3,'western','Вестерн');
INSERT INTO "reviews_genre" VALUES (4,'fantasy','Фэнтези');
INSERT INTO "reviews_genre" VALUES (5,'sci-fi','Фантастика');
INSERT INTO "reviews_genre" VALUES (6,'detective','Детектив');
INSERT INTO "reviews_genre" VALUES (7,'thriller','Триллер');
INSERT INTO "reviews_genre" VALUES (8,'tale','Сказка');
INSERT INTO "reviews_genre" VALUES (9,'gonzo','Гонзо');
INSERT INTO "reviews_genre" VALUES (10,'roman','Роман');
INSERT INTO "reviews_genre" VALUES (11,'ballad','Баллада');
INSERT INTO "reviews_genre" VALUES (12,'rock-n-roll','Rock-n-roll');
INSERT INTO "reviews_genre" VALUES (13,'classical','Классика');
INSERT INTO "reviews_genre" VALUES (14,'rock','Рок');
INSERT INTO "reviews_genre" VALUES (15,'chanson','Шансон');
INSERT INTO "reviews_title" VALUES (1,'Побег из Шоушенка',NULL,1994,1);
INSERT INTO "reviews_title" VALUES (2,'Крестный отец',NULL,1972,1);
INSERT INTO "reviews_title" VALUES (3,'12 разгневанных мужчин',NULL,1957,1);
INSERT INTO "reviews_title" VALUES (4,'Список Шиндлера',NULL,1993,1);
INSERT INTO "reviews_title" VALUES (5,'Криминальное чтиво',NULL,1994,1);
INSERT INTO "reviews_title" VALUES (6,'Хороший, плохой, злой',NULL,1966,1);
INSERT INTO "reviews_title" VALUES (7,'Властелин колец: Братство кольца',NULL,2001,1);
INSERT INTO "reviews_title" VALUES (8,'Бойцовский клуб',NULL,1999,1);
INSERT INTO "reviews_title" VALUES (9,'Форрест Гамп',NULL,1994,1);
INSERT INTO "reviews_title" VALUES (10,'Звёздные войны. Эпизод 5: Империя наносит ответный удар',NULL,1980,1);
INSERT INTO "reviews_title" VALUES (11,'Властелин колец: Две крепости',NULL,2002,1);
INSERT INTO "reviews_title" VALUES (12,'Матрица',NULL,1999,1);
INSERT INTO "reviews_title" VALUES (13,'Пролетая над гнездом кукушки',NULL,1975,1);
INSERT INTO "reviews_title" VALUES (14,'Назад в будущее',NULL,1985,1);
INSERT INTO "reviews_title" VALUES (15,'Операция «Ы» и другие приключения Шурика',NULL,1965,1);
INSERT INTO "reviews_title" VALUES (16,'Карты, деньги, два ствола',NULL,1998,1);
INSERT INTO "reviews_title" VALUES (17,'Джентльмены удачи',NULL,1971,1);
INSERT INTO "reviews_title" VALUES (18,'Джанго освобожденный',NULL,2012,1);
INSERT INTO "reviews_title" VALUES (19,'Generation П',NULL,2011,1);
INSERT INTO "reviews_title" VALUES (20,'Колобок',NULL,1873,2);
INSERT INTO "reviews_title" VALUES (21,'Страх и ненависть в Лас-Вегасе',NULL,1971,2);
INSERT INTO "reviews_title" VALUES (22,'Война и мир',NULL,1865,2);
INSERT INTO "reviews_title" VALUES (23,'Улисс',NULL,1918,2);
INSERT INTO "reviews_title" VALUES (24,'Generation П',NULL,1999,2);
INSERT INTO "reviews_title" VALUES (25,'Винни Пух и все-все-все',NULL,1926,2);
INSERT INTO "reviews_title" VALUES (26,'Стас Михайлов - Позывные на любовь',NULL,2004,3);
INSERT INTO "reviews_title" VALUES (27,'Led Zeppelin — Stairway to Heaven',NULL,1971,3);
INSERT INTO "reviews_title" VALUES (28,'Jethro Tull - Aqualung',NULL,1971,3);
INSERT INTO "reviews_title" VALUES (29,'Elvis Presley - Blue Suede Shoes',NULL,1955,3);
INSERT INTO "reviews_title" VALUES (30,'Deep Purple — Smoke on the Water',NULL,1971,3);
INSERT INTO "reviews_title" VALUES (31,'Моцарт - Турецкий марш',NULL,1784,3);
INSERT INTO "reviews_title" VALUES (32,'Бах. Оркестровая Сюита №2 си минор',NULL,1739,3);
INSERT INTO "reviews_title_genre" VALUES (1,1,1);
INSERT INTO "reviews_title_genre" VALUES (2,2,1);
INSERT INTO "reviews_title_genre" VALUES (3,3,1);
INSERT INTO "reviews_title_genre" VALUES (4,4,1);
INSERT INTO "reviews_title_genre" VALUES (5,5,2);
INSERT INTO "reviews_title_genre" VALUES (6,5,6);
INSERT INTO "reviews_title_genre" VALUES (7,5,7);
INSERT INTO "reviews_title_genre" VALUES (8,6,3);
INSERT INTO "reviews_title_genre" VALUES (9,7,4);
INSERT INTO "reviews_title_genre" VALUES (10,8,7);
INSERT INTO "reviews_title_genre" VALUES (11,9,1);
INSERT INTO "reviews_title_genre" VALUES (12,9,2);
INSERT INTO "reviews_title_genre" VALUES (13,10,4);
INSERT INTO "reviews_title_genre" VALUES (14,11,4);
INSERT INTO "reviews_title_genre" VALUES (15,12,1);
INSERT INTO "reviews_title_genre" VALUES (16,12,5);
INSERT INTO "reviews_title_genre" VALUES (17,12,6);
INSERT INTO "reviews_title_genre" VALUES (18,12,8);
INSERT INTO "reviews_title_genre" VALUES (19,13,1);
INSERT INTO "reviews_title_genre" VALUES (20,14,5);
INSERT INTO "reviews_title_genre" VALUES (21,15,2);
INSERT INTO "reviews_title_genre" VALUES (22,15,6);
INSERT INTO "reviews_title_genre" VALUES (23,15,8);
INSERT INTO "reviews_title_genre" VALUES (24,16,2);
INSERT INTO "reviews_title_genre" VALUES (25,17,2);
INSERT INTO "reviews_title_genre" VALUES (26,18,1);
INSERT INTO "reviews_title_genre" VALUES (27,19,1);
INSERT INTO "reviews_title_genre" VALUES (28,20,7);
INSERT INTO "reviews_title_genre" VALUES (29,20,8);
INSERT INTO "reviews_title_genre" VALUES (30,21,9);
INSERT INTO "reviews_title_genre" VALUES (31,22,10);
INSERT INTO "reviews_title_genre" VALUES (32,23,10);
INSERT INTO "reviews_title_genre" VALUES (33,24,10);
INSERT INTO "reviews_title_genre" VALUES (34,25,8);
INSERT INTO "reviews_title_genre" VALUES (35,26,15);
INSERT INTO "reviews_title_genre" VALUES (36,27,11);
INSERT INTO "reviews_title_genre" VALUES (37,27,14);
INSERT INTO "reviews_title_genre" VALUES (38,28,11);
INSERT INTO "reviews_title_genre" VALUES (39,29,12);
INSERT INTO "reviews_title_genre" VALUES (40,30,14);
INSERT INTO "reviews_title_genre" VALUES (41,31,13);
INSERT INTO "reviews_title_genre" VALUES (42,32,13);
INSERT INTO "reviews_comment" VALUES (1,'Ничего подобного, в фильме всё не так, и программирование тут вообще ни при чём!','2020-01-13T23:20:02.422',102,6);
INSERT INTO "reviews_comment" VALUES (2,'Ну надо же, не нашлось ничего лучшего, кроме как прокомментировать разговор про гамбургеры, будто в фильме ничего важнее этого нет','2020-01-13T23:20:02.422',101,6);
INSERT INTO "reviews_comment" VALUES (3,'Кстати, а что такое "четверть фунта"? В граммах это сколько?','2020-01-13T23:20:02.422',103,6);
INSERT INTO "reviews_review" VALUES (1,'Ставлю десять звёзд!
...Эти голоса были чище и светлее тех, о которых мечтали в этом сером, убогом месте. Как будто две птички влетели и своими голосами развеяли стены наших клеток, и на короткий миг каждый человек в Шоушенке почувствовал себя свободным.',10,'25.09.2019 0:08',100,1);
INSERT INTO "reviews_review" VALUES (2,'Не привыкай
«Эти стены имеют одно свойство: сначала ты их ненавидишь, потом привыкаешь, а потом не можешь без них жить»',10,'25.09.2019 0:08',101,1);
INSERT INTO "reviews_review" VALUES (3,'Фильм, разобранный на цитаты, достоин высшей оценки. Десять с плюсом (жаль, тут плюса нет)
"Ты пришел и говоришь: "Дон Корлеоне, мне нужна справедливость". Но ты просишь без уважения, ты не предлагаешь дружбу, ты даже не назвал меня Крестным Отцом."',10,'25.09.2019 0:08',102,2);
INSERT INTO "reviews_review" VALUES (4,'Жестокий, жестокий, жестокий мир, не о таком мечтали мы в детстве!!111
***Отец сделал ему предложение, от которого он не смог отказаться. Лука Брази держал пистолет у его виска, и отец предложил выбор: либо на контракте мозги, либо подпись.***',1,'25.09.2019 0:08',103,2);
INSERT INTO "reviews_review" VALUES (5,'Это мои соседи! Ставлю три звезды за то, что они дважды отдавили мне окном пальцы:
----------------------
— Вы живёте в плохом районе?
— Не то слово. Однажды с нашей улицы угнали полицейскую машину с двумя полицейскими. В дом всё время лезут воры. Каждый раз, как я пытаюсь закрыть окно, прищемляю кому-нибудь пальцы.',3,'25.09.2019 0:08',104,2);
INSERT INTO "reviews_review" VALUES (6,'Всё, как в разных языках программирования! В основном — похоже, но вот эти маленькие различия выводят из себя. 
Великий фильм на все случаи жизни!
=====================================================
— А знаешь, как в Париже называют четвертьфунтовый чизбургер?
— Что, они не зовут его четвертьфунтовый чизбургер?
— У них там метрическая система. Они вообще там не понимают, что за хрен четверть фунта.
— И как они его зовут?
— Они зовут его «Роял чизбургер».
— «Роял чизбургер»? А как же тогда они зовут «Биг Мак»?
— «Биг Мак» это «Биг Мак», только они называют его «Лё Биг Мак».',8,'25.09.2019 0:08',100,5);
INSERT INTO "reviews_review" VALUES (7,'Ничего не понятно. Они там что, страницы сценария перепутали? Его сперва убили, а потом он опять жив, а они сперва в футболках, потом в костюмах, а потом опять в футболках. Ерунда полная',1,'25.09.2019 0:08',101,5);
INSERT INTO "reviews_review" VALUES (8,'Очень поучительный фильм о том, что такое хорошо, что такое плохо и почему не надо читать в туалете.
Твердая восьмёрка',8,'25.09.2019 0:08',102,5);
INSERT INTO "reviews_review" VALUES (9,'Посмотрел фильм. 
— На свете есть два типа людей: те, кто копает и те, у кого заряжен револьвер.
Пойду копать, как велел Клинт. 
Девять баллов.',9,'25.09.2019 0:08',103,6);
INSERT INTO "reviews_review" VALUES (10,'Вечная проблема всех злодеев, болтающих-болтающих-болтающих вместо того, чтобы просто застрелить противника, одним махом решена в этой сцене.
За одно это фильм заслуживает высшего балла
"Пришел стрелять - стреляй, а не болтай!"',10,'25.09.2019 0:08',104,6);
INSERT INTO "reviews_review" VALUES (12,'Недавно именно так я изобрёл вечный двигатель! Чистая правда в фильме, почему он назван "фантастикой", это же полнейший реализм!
Вот цитата. Но зачем ему часы в уборной?!
— В тот день я изобрёл путешествие во времени! Как сейчас помню… Я стоял на унитазе и вешал часы. Вдруг подскользнулся, ударился головой о раковину',8,'25.09.2019 0:08',101,14);
INSERT INTO "reviews_review" VALUES (13,'Великий фильм, жаль только, что будущее, которое в нём показано, уже в прошлом. Но проблемы всё теже, вот как эта, например: «Док, послушай, всё, что нам нужно — это немного плутония!»
Всегда не хватает какой-нибудь мелочи. Семёрка за то, что будущее оказалось не таким, как обещали.',7,'25.09.2019 0:08',102,14);
INSERT INTO "reviews_review" VALUES (14,'Будущее выглядит странно и неожиданно, тоже мне, бином Ньютона. Но диалог прекрасен, и за это не стану сильно минусовать.
-- Then tell me, future boy, who''s President of the United States in 1985?
-- Ronald Reagan.
-- Ronald Reagan? The actor? Then who''s vice president? Jerry Lewis?',4,'25.09.2019 0:08',103,14);
INSERT INTO "reviews_review" VALUES (15,'Неужели из тюрьмы так легко было сбежать? Раз - и ты на свободе. Да, побег из Шоушенка пришлось готовить немного дольше. Пять за соцреализм',5,'25.09.2019 0:08',104,17);
INSERT INTO "reviews_review" VALUES (16,'Сходила в кино, решила написать: драйв и огонь, но иногда какой-то бред на экране. В середине фильма просто отличные диалоги! Пусть будет 7',7,'25.09.2019 0:08',100,3);
INSERT INTO "reviews_review" VALUES (17,'Смотрел, не отрываясь, хочу описать свои впечатления. По моему мнению, сценарий подкачал, зато подбор актёров - супер. Начало немного затянуто. Оператору - Оскара! Всё остальное - не очень. Фильм тянет на 8 из 10',8,'25.09.2019 0:08',101,3);
INSERT INTO "reviews_review" VALUES (18,'Скачал, посмотрел, думаю, что актёры так себе, сценарий хороший. Диалоги прекрасные, так что пусть будет восемь звезд',8,'25.09.2019 0:08',102,4);
INSERT INTO "reviews_review" VALUES (19,'Посмотрел. По моему мнению, актёры так себе, но сценарий хороший. Первую половину фильма можно спать, не опасаясь, что что-то пропустишь. Не раздумывая, ставлю уверенную десятку',10,'25.09.2019 0:08',103,4);
INSERT INTO "reviews_review" VALUES (20,'Скажу тем, кто ещё не смотрел: если бы я был режиссёром этого фильма - я бы не гордился. Оператора уволить, фильм получился так себе, но один раз посмотреть - сойдёт. Авторы честно заслужили 5 из 10',5,'25.09.2019 0:08',104,7);
INSERT INTO "reviews_review" VALUES (21,'Скачал, посмотрел, думаю, что сценарий подкачал, зато подбор актёров - супер. Начало немного затянуто, да и вообще не очень. Фильм едва тянет на 4',4,'25.09.2019 0:08',100,7);
INSERT INTO "reviews_review" VALUES (22,'Мне кажется, что я впустую потерял время. Ставлю 2',2,'25.09.2019 0:08',101,8);
INSERT INTO "reviews_review" VALUES (23,'Посмотрела. Актёры так себе, сценарий хороший. Уснула к середине. Не раздумывая, ставлю двойку',2,'25.09.2019 0:08',102,8);
INSERT INTO "reviews_review" VALUES (24,'Все очень долго ждали премьеру фильма,и наконец дождались.Фильм отличный,добрый,смотрится почти на одном дыхании,с завязанным сюжетом и не менее крутой музыкой.Кино очень понравилось!!!Всем советую.',10,'25.09.2019 0:08',103,9);
INSERT INTO "reviews_review" VALUES (25,'Отстой-фильм. Не ходите',1,'25.09.2019 0:08',104,9);
INSERT INTO "reviews_review" VALUES (26,'Для людей, которые хотят посмеяться и получить море эмоций, тот самый фильм. Мне очень понравился.',10,'25.09.2019 0:08',100,9);
INSERT INTO "reviews_review" VALUES (27,'Первый раз в жизни решила написать отзыв,чтобы предостеречь от потери денег на билет и траты времени на просмотр. К игре актеров претензий нет',2,'25.09.2019 0:08',101,10);
INSERT INTO "reviews_review" VALUES (28,'2 часа смотрятся на одном дыхании. Спецэффекты на уровне фильмов Марвела. Смотрели всей семьей. Посмотрел несколько отзывов, понял , что фильм стоит посмотреть',10,'25.09.2019 0:08',102,10);
INSERT INTO "reviews_review" VALUES (29,'Действия персонажей вызывают постоянный вопросы - что и зачем они это делают. Логики просто нет. После половины фильма уже хочется уйти',1,'25.09.2019 0:08',103,11);
INSERT INTO "reviews_review" VALUES (30,'Лучший фильм, однозначно. Шедевр. Но следует понимать, что это не кино под пиво для молодежи. Стильно снято, на одном дыхании
смотрится, персонажи великолепны',10,'25.09.2019 0:08',104,11);
INSERT INTO "reviews_review" VALUES (31,'Тупее не видел, смотреть не интересно скучняк',1,'25.09.2019 0:08',100,11);
INSERT INTO "reviews_review" VALUES (32,'Фильм интересный,но не доработанный.Остроты сюжета не хватает',8,'25.09.2019 0:08',101,12);
INSERT INTO "reviews_review" VALUES (33,'Самая сильная картина за последнее время. Фильм заставляет плакать, радоваться, грустить, держит в напряжении',10,'25.09.2019 0:08',102,12);
INSERT INTO "reviews_review" VALUES (34,'С огромным удовольствием сходила в кинотеатр. Одноразовые фильмы, названия которых забываешь на выходе из дверей кинозала, разочаровывают. И вот настоящий, душевный, жизненный фильм. Игра акторов и сюжет бомбические.',9,'25.09.2019 0:08',103,12);
INSERT INTO "reviews_review" VALUES (35,'Что сказать после просмотра? Ничего. Такое ощущение, что тебя обманули, заставили смотреть за твои деньги на стену',1,'25.09.2019 0:08',104,13);
INSERT INTO "reviews_review" VALUES (36,'Хотелось уйти уже на двадцатой минуте. Неинтересно и нудно. Режиссура не впечатлила, ну просто неинтересно смотреть было',2,'25.09.2019 0:08',100,13);
INSERT INTO "reviews_review" VALUES (37,'Фильм стоит увидеть тем, кому интересно современное кино. Не скучно, не затянуто, понравилась операторская работа, некоторые сцены сделаны на хорошем уровне',8,'25.09.2019 0:08',101,13);
INSERT INTO "reviews_review" VALUES (38,'Муторно и тяжело. Ставлю 2',2,'25.09.2019 0:08',102,15);
INSERT INTO "reviews_review" VALUES (39,'Фильм не оправдал ожиданий. Сплошная каша, слабый сценарий. С трудом досмотрела до конца. Ожидала нечто такого интересного и захватывающее. Полное разочарование. Отдельные несвязные сцены, непонятные диалоги',3,'25.09.2019 0:08',103,15);
INSERT INTO "reviews_review" VALUES (40,'Мне фильм понравился. Все качественно,красиво. Игра актеров, в основном, очень даже. Но слишком много, для меня кровавых сцен,слабонервным просьба не смотреть',9,'25.09.2019 0:08',104,15);
INSERT INTO "reviews_review" VALUES (41,'Зря потерянное время! Эмоции после просмотра, - безысходность, ничего уже не изменишь. Фильм вообще никакой!!!
И поставили его люди бездарные и никчёмные!!!',1,'25.09.2019 0:08',100,16);
INSERT INTO "reviews_review" VALUES (42,'После просмотра разочарование граничит с шоком. Бездарный фильм, как предыдущий от этого же режиссера. Не рекомендую никому! Плохо, неправдоподобно, скомкано снято.',2,'25.09.2019 0:08',101,16);
INSERT INTO "reviews_review" VALUES (43,'Фильм мощный. Главное - не занимать чью-то позицию, а смотреть со стороны. Впервые вижу, чтобы было так детально показаны переживания и эмоции каждого героя. Все на своем месте. Актеры и графика на высоте.',10,'25.09.2019 0:08',102,16);
INSERT INTO "reviews_review" VALUES (44,'Если такой жанр вам по вкусу, то даже не сомневайтесь - бегом в кинотеатр! Фильм - огонь! Интересный сюжет, великолепная игра актёров, съёмки просто супер, да и спецэффекты на высоте',10,'25.09.2019 0:08',103,17);
INSERT INTO "reviews_review" VALUES (45,'Сюжет, мысль, философия, игра актеров, эмоции - блеск! Сюжет динамичный, игра актёров хороша, но не идеальна.',8,'25.09.2019 0:08',104,18);
INSERT INTO "reviews_review" VALUES (46,'Разочарованине, вытащила себя в кино, а тут такое. Реклама шла мноообещающая, а в реальности всё не то',2,'25.09.2019 0:08',100,18);
INSERT INTO "reviews_review" VALUES (47,'Неправдоподобный, нелогичный, бессмысленный фильм. Просто никакой, можете даже не смотреть, сути не уловите. Мне понравился',10,'25.09.2019 0:08',101,19);
INSERT INTO "reviews_review" VALUES (48,'Интересно продуманный фильм, цепляет необычным сюжетом. длинный, что бывает не во всех фильмах. Актёры крутые. В общем, посмотреть можно.',8,'25.09.2019 0:08',102,19);
INSERT INTO "reviews_review" VALUES (49,'Внимательно слежу за всеми новыми изданиями, покупаю каждое. Лучший триллер тысячелетия — это «Колобок»',10,'25.09.2019 0:08',103,20);
INSERT INTO "reviews_review" VALUES (50,'А вот у кипчаков «колобок» — шарик из навоза! И сказка приобретает совсем другой смысл! «Не хитри, а то навоза накушаешься!»',10,'25.09.2019 0:08',104,20);
INSERT INTO "reviews_review" VALUES (51,'Прочла от начала до конца, не отрываясь. Ужасная книга, чему она может научить нашу молодёжь.',1,'25.09.2019 0:08',100,21);
INSERT INTO "reviews_review" VALUES (52,'Суровые американские семидесятые в документальном изложении. Как автор дожил до 2005-го года — загадка. Но роман прекрасный.',10,'25.09.2019 0:08',101,21);
INSERT INTO "reviews_review" VALUES (53,'Многабукуф. Ниасилил. В аннотации написано — «великий роман», так что ставлю максимальную оценку',10,'25.09.2019 0:08',102,22);
INSERT INTO "reviews_review" VALUES (54,'Если такой жанр вам по вкусу, то даже не сомневайтесь: садитесь читать! Роман - огонь! Интересный сюжет, великолепные персонажи, небо Аустерлица и встреча с дубом',10,'25.09.2019 0:08',103,22);
INSERT INTO "reviews_review" VALUES (55,'Я ВиМ в школе читал (заставляли), а потом опять случайно прочёл, и оказалось, что он и правла великий, а не просто так. Не ставлю десятку только в память о школьных мучениях',8,'25.09.2019 0:08',104,22);
INSERT INTO "reviews_review" VALUES (56,'Ничего не понял',3,'25.09.2019 0:08',100,23);
INSERT INTO "reviews_review" VALUES (57,'Не понял вообще ничего',1,'25.09.2019 0:08',101,23);
INSERT INTO "reviews_review" VALUES (58,'Совсем непонятно, но здорово',8,'25.09.2019 0:08',102,23);
INSERT INTO "reviews_review" VALUES (59,'Что это было?! Десятка за уровень непонятности',10,'25.09.2019 0:08',103,23);
INSERT INTO "reviews_review" VALUES (60,'Детально комментировать не буду, но это шедевр',10,'25.09.2019 0:08',104,23);
INSERT INTO "reviews_review" VALUES (63,'Не может быть такого. Это всё придумано, автор попытался обмануть читателя, но мы, читатели, умнее его. Нас вокруг пальца не обведёшь!!',2,'25.09.2019 0:08',102,24);
INSERT INTO "reviews_review" VALUES (64,'Всё совершенно не так, как на самом деле, и в документальной повести это хорошо описано',9,'25.09.2019 0:08',103,24);
INSERT INTO "reviews_review" VALUES (65,'Если бы я только мог на минутку перестать бумкать головой по ступенькам и как следует сосредоточиться — я бы написал прекрасный отзыв. Но увы — сосредоточиться-то мне и некогда: учёба, работа. Просто поставлю пятёрку',10,'25.09.2019 0:08',104,25);
INSERT INTO "reviews_review" VALUES (66,'Это просто «Война и мир» для детей. Читать всем',10,'25.09.2019 0:08',100,25);
INSERT INTO "reviews_review" VALUES (67,'Слушаю и плачу. Плачу, но слушаю',10,'25.09.2019 0:08',101,26);
INSERT INTO "reviews_review" VALUES (68,'Какой-то непонятный шум. Неужели это кто-то слушает?',1,'25.09.2019 0:08',102,27);
INSERT INTO "reviews_review" VALUES (69,'Ничего не понятно. О чём эта песня, чему она учит?',2,'25.09.2019 0:08',103,27);
INSERT INTO "reviews_review" VALUES (70,'Йэн Андерсон великий!!!!!!!!1111',10,'25.09.2019 0:08',104,28);
INSERT INTO "reviews_review" VALUES (71,'Неужели песню про аквалангистов перевели на английский?! Ну наконец-то! Аквалангисты — это хорошо!',10,'25.09.2019 0:08',100,28);
INSERT INTO "reviews_review" VALUES (72,'Мы прыгали, вертелись и кружились так, что пол ходил ходуном!',10,'25.09.2019 0:08',101,29);
INSERT INTO "reviews_review" VALUES (73,'Это единственный риф, который я умею играть на своей супердорогой гитаре! Моя любимая песня',10,'25.09.2019 0:08',104,30);
INSERT INTO "reviews_review" VALUES (74,'Странно: Моцарт - австриец, а марш - турецкий. Не понимаю, как так вышло. Звучит красиво, но за географическую путаницу ставлю восемь',8,'25.09.2019 0:08',100,31);
INSERT INTO "reviews_review" VALUES (75,'Бах forever. Это вам не три аккорда на гитаре, как у смок он зе вотер',10,'25.09.2019 0:08',102,32);
COMMIT;