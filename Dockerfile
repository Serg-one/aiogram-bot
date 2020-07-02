FROM python:3.7-slim

WORKDIR /aiogram-bot-template

COPY requirements.txt /aiogram-bot-template/
RUN pip install -r /aiogram-bot-template/requirements.txt
COPY . /aiogram-bot-template/

CMD python3 /aiogram-bot-template/app.py
