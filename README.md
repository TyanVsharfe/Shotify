# Сервис для получения скриншота любого сайта.

## Установка
Склонируйте репозиторий
```shell
git clone https://github.com/TyanVsharfe/Shotify.git
```
Создайте в корне проекта файл .env в котором укажите следующие поля:
```
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_NAME=screenshot_db

MINIO_ENDPOINT=http://minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin

SELENIUM_HOST=selenium
```

Чтобы создать и запустить контейнеры в docker введите следующую команду:
```shell
docker compose up -d
```

## Использование
### API
В данном проекте представлен endpoint http://127.0.0.1:8000/screenshot

## Пример
![image](https://github.com/user-attachments/assets/81fd18a7-a292-41e7-a65d-2f749c164197)
![{3924061F-BF05-4CE7-8AD3-19733D57A0AA}](https://github.com/user-attachments/assets/7c6e2018-e1fe-498a-a57e-9ce2f0bca32f)]
