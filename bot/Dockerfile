FROM python:3.13-slim
RUN pip install --upgrade pip

RUN adduser --disabled-login --disabled-password bot
USER bot

WORKDIR /home/bot
COPY --chown=bot:bot ./bot/requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

WORKDIR /home
COPY --chown=bot:bot . .

WORKDIR /home/bot
CMD ["python", "-u", "main.py"]
