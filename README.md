# Проект: Philology Bot

### Бот предназначенный проводить тестирование на знание правил русского языка

Бот позволяет пользователям тестировать свои знания русского языка, оценивая правильность вводимого ответа. Для владельца бота предусмотрена админ-панель позволяющая осуществлять специальные действия, в том числе рассылку уведомлений.

## Технологии
 ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
 ![Aiogram]
 ![SQlite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
 
## Запуск бота на удаленном сервере
  1. Получите токен бота у @BotFather
  2. Скопируйте проект на удаленный сервер
  3. В корне проекта создайте файл .env и заполните его следующим образом:
  ```dotenv
  BOT_TOKEN=<токен полученный от @BotFather>
  ADMIN_ID=<Ваш id Telegram(узнать можно тут --> @userinfobot)>
  DEVELOPER_ID=(опционально, если Вы выступаете в проекте в роли разработчика
  ```
  4. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
  5. Установите зависимости 
  ```bash
  pip install -r requirements.txt
  ```
  6. Запустите бота
  ```bash
  python main.py
  ```

## Пример [@бота](https://t.me/NWWCPLBot)