FROM python:3.11

COPY ../requirements.txt ./app/requirements.txt
COPY ../shotify       ./app/shotify

RUN pip install --no-cache-dir -r ./app/requirements.txt

ENV PYTHONPATH=./app

CMD ["python", "-O", "./app/shotify/api/main.py"]