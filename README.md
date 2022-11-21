# Personal Webpage Backend Project
Backend for my personal webpage. It is made in Django python framework and using the Django Rest Framework for the API.

## Install project dependencies
To install the project dependencies, just run the command ```pip install -r requirements.txt``` in the root directory of the project.

## Run the project
First of all you can create a ```.env``` file in the root directory of the project. You can use the ```.env.example``` file as a template. If you don't want to create a ```.env``` file, the project will create a sqlite3 database.

Then you need to run the command ```python manage.py migrate``` to create the database. 

Finally you can run the project with the command ```python manage.py runserver```.