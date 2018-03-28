import os
from .settings import INSTALLED_APPS,BASE_DIR,MIDDLEWARE

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT')
INSTALLED_APPS = INSTALLED_APPS + [
    'raven.contrib.django.raven_compat',
]
SECURE_SSL_REDIRECT=True


import django_heroku
django_heroku.settings(locals(),staticfiles=False)