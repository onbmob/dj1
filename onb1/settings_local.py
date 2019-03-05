
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djlocal',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DEBUG = True
