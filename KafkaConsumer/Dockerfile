# Consumer Host
FROM python:3.7-alpine3.9
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN apk --update add bash vim mysql-client mariadb-dev make gcc &&\
  pip3 install -U setuptools &&\
  pip3 install --upgrade pip \
  mysqlclient \
  SQLAlchemy \
  psycopg2 \
  structlog colorama \
  kafka-python
ENTRYPOINT tail -f /dev/null