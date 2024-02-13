FROM python:3.10.10-alpine3.17

WORKDIR /app

RUN apk update \ && apk add --no-cache gcc g++ musl-dev libffi-dev postgresql-dev openssl-dev python3-dev \
    && pip install --upgrade pip

RUN python3 -m venv venv \
    && venv/bin/pip install wheel pybase64

RUN python3 -m pip install --upgrade pip

COPY ./requirements.txt ./

RUN venv/bin/pip install -r requirements.txt


COPY . .

RUN source venv/bin/activate && pip install -r requirements.txt

RUN pip install -r requirements.txt

CMD ["python","src/manage.py","runserver","0.0.0.0:8000"]

