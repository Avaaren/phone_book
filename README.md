# phone_book
Project with 2 RESTapi apps - phone book and weather widget

Описание запуска сервера
1) Склонировать или скачать репозиторий
2) Перейти в папку backend -> phone_book
3) Создать виртуальное окружение python командой "python -m venv env" или другими удобными способами
4) Активировать среду "source env\bin\activate" - linux или "env\Scripts\activate" - windows
5) Установить зависимости командой  "pip install -r requirements.txt"
6) Произвести миграции "python manage.py migrate"
7) Сервер готов к запуску "python manage.py runserver" (телефонная книга будет работать)
7.1)*Добавление абонентов осуществляется отправкой post запросов посредством postman либо другой утилиты

Для работы погодного приложения необходим установленный redis
1) Запустите redis командой  redis-server
2) Запустите локальный сервер как описано выше
3) Откройте 2 новые вкладки терминала
4) В первой перейдите в ту же папку, что и локальный сервер, активируйте виртуальное окружение и пропишите команду
"celery -A phone_book worker -l info"
(в винде понадобится установить дополнительный пакет "pip install gevent" и прописать после "-l info -P gevent")

5) Во второй вкладке сделайте все тоже самое но пропишите "celery -A phone_book beat -l info"
(Будет происходить обновление погоды каждые 30 минут)

Описание API
API содержит два приложения - Телефонная книга и Погодное приложение.
Используется БД SQLite3
Описание Телефонной книги:
Приложение содержит две таблицы - Абонент и Номер. Абонент может иметь несколько номеров, как домашних, так и мобильных.
Поддерживает CRUD операции как над абонентом, так и над номером.
1) Для доступа к главной странице телефонной книги необходимо в адресной строке прописать http://127.0.0.1:8000/api
Главная страница отдает список всех абонентов в формате:
    {
        "id",
        "phones": [
        {
             "id",
             "number",
             "type_of_number""
         },
            ],
        "name",
        "surname",
        "patronymic_name",
        "address",
        "city"
    },
Также с главной страницы возможно добавление нового контакта. Для этого необходимо на этот же адрес отправить post
запрос любой утилитой типа postman в формате:
{
        "phones": [
            {
                "number": "88005553535",
                "type_of_number": "Мобильный"
            },
            {
                "number": "987456321",
                "type_of_number": "Мобильный"
            }
        ],
        "name": "Витя",
        "surname": "Карпенко",
        "patronymic_name": "Серогин",
        "address": "ул.Петра 22",
        "city": "Минск"
 }
2) Для редактирования, удаления пользователя необходимо перейти по адресу http://127.0.0.1:8000/api/<id польз>
На данный url возможна отправка GET - получение, PUT - редактирование и DELETE - удаление, запросов.
3) Для добавления номера для существующего абонента необходимо перейти по адресу http://127.0.0.1:8000/api/<id польз>/add_number
Данный url поддерживает GET - отдает список номеров и POST - создание нового номера запросов. 
4) Для редактирования, удаления номера конкретного пользователя необходимо перейти
по адресу http://127.0.0.1:8000/api/<id польз>/<id номера>
На данный url возможна отправка GET - получение, PUT - редактирование и DELETE - удаление, запросов.


Описание погодного приложения:
Содержит две таблицы - Погода и Город. Каждые пол часа приложение собирает данные о погоде и отдает их пользователю.
Поддерживает добавление, редактирование и удаление городов. При добавлении нового города автоматически собираются данные
о его погоде. Для существующих городов данные обновляются раз в пол часа.
1) Для получения списка с погодой в существующих городах необходимо перейти по адресу http://127.0.0.1:8000/api/weather
Будет получен список погоды формата 
   [{     "id",
        "city_name",
        "temperature",
        "wind_speed",
        "weather_condition",
        "weather_icon_id",
        "time""
    },
    {
        "id",
        "city_name",
        "temperature",
        "wind_speed",
        "weather_condition",
        "weather_icon_id",
        "time""
    }]
    
2) Для добавления города и получения для него погоды необходимо перейти по адресу http://127.0.0.1:8000/api/weather/add_city
Поддерживает два типа запросов - GET - получение списка существующих городов и POST - создание нового города.
3) Для доступа к существующему городу необходимо перейти по адресу http://127.0.0.1:8000/api/weather/<id города>
На данный url возможна отправка GET - получение, PUT - редактирование и DELETE - удаление, запросов.
