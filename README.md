# Top Charts
Агрегатор музыкальных чартов различных радиостанций\
**Django 3.1** + **sqlite3** + **PostgreSQL** + **Docker** + **DjangoRestFramework** + **BeautifulSoup** + **custom html+css**.

Реализовал сбор данных (парсинг чатов радиостанций) 
с помощью запуска файла run_scraping.py в корне проекта.\
Скрипт собирает чарты по добавленным станциям и складывает 
в базу через модели Django.\
Настроил панель администратора и переписал её оформление (css).\
Реализовал API на **DjangoRestFramework** с базовыми возможностями.

Добавил docker-compose и Dockerfile. 
Можно собрать контейнер с этим проектом и в роли БД postgresql.\
Создаётся django superuser с дефолтными именем и паролем `Admin`\
Сборка образа и запуск:\
`docker-compose up -d --build`

Возможна работа с внутренней базой sqlite без docker: \
`python manage.py runserver`

Главная страница представляет из себя карточки с названием станции. 
При наведении на неё - карточка разворачивается и с обратной стороны 
свежий чарт в сокращенной форме (top 5) и подписью сколько дней назад 
он обновился. При нажатии на карточку осуществляется переход на страницу 
с выбором чарта за предыдущие недели данной станции.

![](top_charts.gif)

##TODO:
  * добавить регистрацию пользователей,
  * автоматизировать запуск сбора данных,
  * писать ошибки в log,
  * реализовать подписку на обновлённые чарты,
  * реализовать форму добавлении чарта желаемой станции,
  * написать тесты,
  * добавить станции и парсеров чартов (record, hitfm, ...),
  * расширить БД
    * расширить модели (например, url радиостанции),
    * добавить модели (например, страны и жанры),
    * добавить модель ParseError и записывать ошибки парсинга,
  * поработать над фронтом,
  * расширить возможности API (добавить разрешения и запросы).
