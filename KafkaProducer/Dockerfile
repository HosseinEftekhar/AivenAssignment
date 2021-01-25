#Producer Host
FROM python:3.7-alpine3.9
RUN apk --update add bash vim mysql-client mariadb-dev make gcc && \
  pip3 install -U setuptools && \
  pip3 install --upgrade pip \
  requests \
  structlog colorama \
  kafka-python
ENTRYPOINT tail  -f /dev/null