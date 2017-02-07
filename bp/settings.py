# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'gl(_blk13s#8&)eoup(jx^rab-&tfnzvmmi%#xi*%vb&7mph#k'

DEBUG = True

ALLOWED_HOSTS = [u'127.0.0.1']

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_geoip',

    'mptt',
    'django_mptt_admin',
    'ckeditor',
    'haystack',
    'sorl.thumbnail',
    'django_filters',

    'app',
    'app.pages',
    'app.search',
    'app.feedback_form',
    'app.slider',
    'app.filter',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bp',
        'USER': 'bp_user',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        # 'PORT': '',
    }
}

# CKEditor settings
CKEDITOR_UPLOAD_PATH = 'ckeditor_uploads'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Source'],
            ['Bold', 'Italic', 'Underline', 'Strike',
             'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['Link', 'Unlink'],
            ['Image', 'Flash', 'SpecialChar'],
            '/',
            ['Format', 'TextColor'],
            ['Maximize', 'ShowBlocks'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Undo', 'Redo', 'Find', 'Replace', 'SelectAll', 'RemoveFormat'],
        ],
        'width': 840,
        'height': 300,
        'toolbarCanCollapse': False,
        'autoParagraph': False,
        'protectedSource': ['.*'],  # allow all source code, doesn't control anything
        'allowedContent': True,
        'allowedContentRules': '/^(*[*]{*}(*))/i',
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT = False

STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'

# SEARCH
WHOOSH_INDEX_DIR = 'whoosh_index'

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
FEEDBACK_EMAIL = "druhound51@gmail.com"
SERVER_EMAIL = "seversait@yandex.ru"
