# Steam clone

## Установка

1. Склонируй репозиторий проекта:

`git clone https://github.com/Headsman-4899/Steam_API.git`

2. Перейди в каталог проекта:

`cd Steam`

3. Установи зависимости, используя команду:

`pipenv install`

4. Примени миграции базы данных:

`python manage.py migrate`


## Использование

1. Запусти разработческий сервер Django:

`python manage.py runserver`


2. Открой веб-браузер и перейдите по адресу `http://localhost:8000/admin/`


3. login: admin, password: admin