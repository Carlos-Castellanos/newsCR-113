# Mini challenge 1

### Set the newspaper project up

#### During this first phase, we'll focus our attention on setup and configuration.

1. Create a new django project in this directory (news) that uses this directory as it's containing folder.
2. Create the following apps:
2.1. accounts
2.2. articles
2.3. pages

        django-admin startproject config .
        python3 manage.py startapp accounts
        python3 manage.py startapp articles
        python3 manage.py startapp pages

3. Modify config.settings to include the following:
3.1. Configure the allowed hosts list (bear in mind, we'll be deploying to heroku later)
        ALLOWED_HOSTS = ["localhost","127.0.0.1",".herokuapp.com"]

3.2. Configure the SECRET_KEY and DEBUG settings to read from environment variables.
    pip3 install "environs[django]"

    from environs import Env
    env = Env()
    env.read_env()

    SECRET_KEY = env.str("SECRET_KEY")
    DEBUG = env.bool("DEBUG", default=False)
    create .env file
    export DEBUG=True
    export SECRET_KEY=z7C0EJzFEpvvF0nig5sSNX-YMAE7uSCMiheyu8C35OU

3.3. Configure the templates directories.
    'DIRS': [str(BASE_DIR.joinpath("templates"))],
3.4. Configure static and staticfiles directories (consider using whitenoise).
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
    STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

    pip3 install whitenoise
    pip3 install gunicorn
    create Procfile
        web: gunicorn config.wsgi --log-file - 

4. *IMPORTANT: Don't run the migrations.*
5. Create the following models in the accounts/models.py file:



from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
