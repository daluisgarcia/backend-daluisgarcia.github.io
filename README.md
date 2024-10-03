# Projects portfolio backend

This project is a REST API that allows to manage projects and their images. The project is developed with Django and Django Rest Framework. This API is being consumed by the [daluisgarcia.github.io](https://github.com/daluisgarcia/daluisgarcia.github.io) repository.

## Install project for development

To install the project for development you need to have docker installed in your machine. Having docker installed, you can run the command ```docker-compose up``` in the root directory of the project. I recommend to create a `docker-compose.override.yml` file to set the environment variables and also a development running comand.  You can use the following template:

```yml
services:
    db:
        environment:
        MYSQL_ROOT_PASSWORD: ""
        MYSQL_DATABASE: "portfolio"
    app:
        command:
            - /bin/sh
            - -c
            - |
                python manage.py runserver 0.0.0.0:8000
        volumes:
            - .:/app/
        environment:
            - DEBUG=True
            - SECRET_KEY=""
            - DATABASE_ENGINE=mysql
            - DATABASE_NAME=portfolio
            - DATABASE_USER=root
            - DATABASE_PASSWORD=
            - DATABASE_HOST=db
            - DATABASE_PORT=3306
            - DEBUG=True
            - ALLOWED_HOSTS=*
```

To make migrations you need to run the command ```docker-compose exec app poetry run python manage.py migrate```.

When the migration is complited, you can create a superuser with the command ```docker-compose exec app poetry run python manage.py createsuperuser```.

## Install project for production

To install the project for production you need to have docker installed in the server. Having docker installed, you can run the command ```docker compose up -d``` in the root directory of the project. I recommend to create a `docker-compose.override.yml` file to set the environment variables. You can use the following template:

```yml
services:
    db:
        environment:
        MYSQL_ROOT_PASSWORD: ""
        MYSQL_DATABASE: "portfolio"
    app:
        volumes:
            - .:/app/
        environment:
            - DEBUG=True
            - SECRET_KEY=""
            - DATABASE_ENGINE=mysql
            - DATABASE_NAME=portfolio
            - DATABASE_USER=root
            - DATABASE_PASSWORD=
            - DATABASE_HOST=db
            - DATABASE_PORT=3306
            - DEBUG=True
            - ALLOWED_HOSTS=*
```

After the container is running, you need to make the migrations with the command ```docker-compose exec app poetry run python manage.py migrate```.

When the migration is complited, you can create a superuser with the command ```docker-compose exec app poetry run python manage.py createsuperuser```.

To make statuc files available you need to run the command ```docker-compose exec app poetry run python manage.py collectstatic```.

## Run the project

First of all you can create a ```.env``` file in the root directory of the project. You can use the ```.env.example``` file as a template. If you don't want to create a ```.env``` file, the project will create a sqlite3 database.

Then you need to run the command ```python manage.py migrate``` to create the database.

When the migration is complited, you can create a superuser with the command ```python manage.py createsuperuser```.

Finally you can run the project with the command ```python manage.py runserver```.
