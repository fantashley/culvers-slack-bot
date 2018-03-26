FROM python:3

WORKDIR /usr/src/app

COPY app/ ./

RUN pip install pipenv && pipenv install

CMD [ "pipenv", "run", "python", "./app.py" ]
