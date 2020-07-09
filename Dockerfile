#FROM python:latest
#
#RUN mkdir /scr
#WORKDIR /scr
#COPY . /scr
#RUN pip install -r requirements.txt

WORKDIR /aiogram-bot-template

COPY requirements.txt /aiogram-bot-template/
RUN pip install -r /aiogram-bot-template/requirements.txt
COPY . /aiogram-bot-template/

CMD python3 /aiogram-bot-template/app.py
