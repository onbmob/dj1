INSTALLED_APPS = [
    'status.apps.StatusConfig',
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

DATABASE_ROUTERS = ['onb1.dbrouter.DbRouter', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djlocal',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'status': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_users',
        'USER': 'web_users',
        'PASSWORD': 'users911',
        'HOST': '80.92.233.198',
        'PORT': '13306',
    },
    'dj2local': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj2local',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DEBUG = True