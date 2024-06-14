# test_settings.py
from .settings import *

SECRET_KEY = 'django-insecure-t&3f4^*$+zxk0zzmg$exb#q3)^@pku2i9676-10@ietkn8d(%-'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

CLOUD_NAME = 'chosen1'
PAYSTACK_SEC_KEY = 'sk_test_ee0e3b910e862b2e6ac71aa21330546b0cdeb445'
PAYSTACK_PUB_KEY = 'pk_test_6277247420fe709bbf29d52a5f7552fe0e8753d7'
API_KEY = '259953999733973'
API_SECRET = 'BIhcZhZbpIz8zYAYuidnLTRAZoo'
