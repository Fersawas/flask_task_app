# TASKS
## Описание проекта
Проект Tasks позволяет создавать заметки/задания с возможностью их просмотра и редактирования.
### Содержанеие

- [Технологии](#tech)
- [Начало работы](#begining)
- [Запуск проекта](#turn_on)
- [Запуск тестов](#tests)
- [FAQ](#faq)
- [Комнада проекта](#team)

## <a name="tech">Технологии</a>

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [MySQL](https://www.mysql.com/)
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/index.html)

## <a name="begining">Начало работы</a>

### Начало работы

Активируйте вирутальное окржуние:

```
python -m venv venv
```

### Установка зависимостей

Активируйте виртуальное окружение

```
source venv/sqripts/activate
```

Установите зависимости из файла *requirements.txt*:

```
pip install -r requirements.txt
```

Если вы работаете локально, в файле .env укажите:
*.env*
```
USER = 'your_mysql_username'
PASSWORD = 'your_mysql_password'
```

### Создание базы данных

Запустите create_database.py:

```
python create_database.py
```

## <a name="turn_on">Запуск проекта</a>

Зайти в корневую директорию. 
Запустите app.py:

```
python app.py
```

Ваш сайт доступен по адресу /localhost:5000/

### Доступные эндпоинты

Для просмотра доступных эндпоинтов перейдите на:
'http://localhost:5000/tasks/doc'

Эндпоинты в соответсвии с тз:
- '/tasks/' - список заданий
- '/tasks/<int:pk>/' - конкретное задание

## <a name="tests">Запуск тестов</a>

Для запуска тестов в корневой директории проекта введите:

'''
pytest
'''

## <a name="team">Команда проектка</a>

- Паршин Денис - разработчик
