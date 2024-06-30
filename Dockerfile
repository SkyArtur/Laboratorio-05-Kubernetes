FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

ENTRYPOINT gunicorn --bind 0.0.0.0:8080 siteSetup.wsgi

EXPOSE 8080
