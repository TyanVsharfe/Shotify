FROM python:3.11

COPY ../requirements.txt ./app/requirements.txt

RUN pip install -r ./app/requirements.txt

COPY ../shotify ./app/shotify

ENV PYTHONPATH=./app

CMD ["python", "-O", "./app/shotify/api/main.py"]