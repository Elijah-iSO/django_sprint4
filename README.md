# Блогикум.

## Описание
Cоциальная сеть для публикации личных дневников. 
Сайт, на котором пользователь может создать свою страницу и публиковать на ней сообщения («посты»).
Для каждого поста можно указать категорию — например «путешествия», «кулинария» или «python-разработка», а также опционально локацию, с которой связан пост, например «Остров отчаянья» или «Караганда». Пользователь может перейти на страницу любой категории и увидеть все посты, которые к ней относятся.
Пользователи смогут заходить на чужие страницы, читать и комментировать чужие посты. Для своей страницы автор может задать имя и уникальный адрес.
Реализована возможность модерировать записи и блокировать пользователей, если начнут присылать спам.

## Инструкция

1. **Клонируйте репозиторий:**

   ```bash
   git clone git@github.com:Elijah-iSO/django_sprint4.git
   cd django_sprint4
   ```

2. **Создание и активация окружения:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Обновление pip и установка зависимостей:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Создайте и примените миграции:**

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
   
6. **Запустите проект:**

   ```bash
   python3 manage.py runserver
   ```

## Cтек технологий
<span style="display: inline-block; margin-right: 5px;">![alt text](https://img.shields.io/badge/python-3.9-blue)
</span> <span style="display: inline-block; margin-right: 5px;">![alt text](https://img.shields.io/badge/django-4.2-green)
</span> <span style="display: inline-block; margin-right: 5px;">![alt text](https://img.shields.io/badge/bootstrap-5.3-purple)
</span>

## Автор
ILYA OLEYNIKOV
GitHub:	https://github.com/Elijah-iSO
E-mail: oleynikovis@yandex.ru
