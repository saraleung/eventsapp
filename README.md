<<<<<<< HEAD
## Goal

The goal of the take home assignment is to evaluate basic understanding of:

- database
- backend technology
- frontend technology
- source control

## Description

- Database: create the following tables
  - Performer table with a name column
  - Event table that has a name column, datetime column
  - Relationship: an event has many performers
  - For example, the test data:
    - Event name: `Blue Jays vs Chicago Cubs`
    - Performers:
        - `Blue Jays`
        - `Chicago Cubs`

- Website:
  - Using a technology of your choice
  - Build a website to display existing events with their associated performers
  - You will prepopuate the database in advance with the above test data
  - A single web page to view an event and its associating performers. A simple table listing the event and performers is sufficient.
  - Write unit tests for any controller or model code

- SCM:
  - Clone or fork this repo to github or bitbucket

- Hosting (optional):
  - Use heroku to deploy your webapp on heroku.com. You can create a free heroku account to host sites there.
  - Java: https://devcenter.heroku.com/articles/deploying-java
  - PHP: https://devcenter.heroku.com/articles/getting-started-with-php#introduction
  - Python: https://devcenter.heroku.com/articles/getting-started-with-python#introduction
=======
# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.10.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment. 

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
>>>>>>> 82fbf52c120ec5d8a7e1ff05be2f8814a7477275
