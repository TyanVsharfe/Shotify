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
В body post запроса необходимо прописать url вашего сайта, а также указать нужно ли делать свежий скриншот этого сайта (true), или если у данного сайта уже есть скриншот то взять его из бд (false), в последнем случае если скриншота в бд нету, то делается новый. Если сайт будет очень долго прогружаться или url будет неверный, будет возвращена ошибка 404.
```json
{
    "url": "https://math.csu.ru",
    "is_fresh": true
}
```

## Пример
![image](https://github.com/user-attachments/assets/81fd18a7-a292-41e7-a65d-2f749c164197)
![{3924061F-BF05-4CE7-8AD3-19733D57A0AA}](https://github.com/user-attachments/assets/7c6e2018-e1fe-498a-a57e-9ce2f0bca32f)]
![{75136C91-8A2C-4216-89C1-3C01C15E7858}](https://github.com/user-attachments/assets/3fe2a8d5-e012-4e5f-856c-23c62d88d499)

