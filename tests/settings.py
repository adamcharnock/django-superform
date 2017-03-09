import warnings
warnings.simplefilter('always')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

USE_I18N = True
USE_L10N = True

INSTALLED_APPS = [
    'django_superform',
    'tests',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = ()

STATIC_URL = '/static/'

SECRET_KEY = '0'
