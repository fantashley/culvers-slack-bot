FROM python:3

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock culversbot.py app.py ./

RUN pip install pipenv && pipenv install

CMD [ "pipenv", "run", "python", "./app.py" ]
