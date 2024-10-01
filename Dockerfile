FROM python:3.12-slim

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.3

RUN apt-get update && \ 
    apt-get install -y curl && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags` && \
    export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry --version
RUN poetry config virtualenvs.create false

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi
RUN poetry add gunicorn

COPY . /app/

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
