# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'gl(_blk13s#8&)eoup(jx^rab-&tfnzvmmi%#xi*%vb&7mph#k'

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = [u'127.0.0.1']

SITE_ID = 1

INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django_hosts',

    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'googlecharts',

    'mptt',
    'django_mptt_admin',
    'ckeditor_uploader',
    'ckeditor',
    'django_geoip',
    'haystack',
    'sorl.thumbnail',
    'meta',
    'compressor',

    'app',
    'app.pages',
    'app.search',
    'app.feedback_form',
    'app.education',
    'app.currency',
    'app.reviews',
    'app.graphics',
    'app.utm',
    'app.news',
    'app.album',
    'app.parsing',
]

MIDDLEWARE_CLASSES = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'bp.middleware.EducationalCenterMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'bp.urls'

APPEND_SLASH = False

# ADMIN_TOOLS
ADMIN_TOOLS_INDEX_DASHBOARD = 'bp.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_MENU = 'bp.menu.CustomMenu'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'bp.context_processors.locations',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
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
        'PORT': '5432',
    }
}

# CKEditor settings
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_UPLOAD_PATH = 'files/media'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'toolbarCanCollapse': False,
        'autoParagraph': False,
        'protectedSource': ['.*'],  # allow all source code, doesn't control anything
        'allowedContent': True,
        'allowedContentRules': '/^(*[*]{*}(*))/i',
    },
}
CONTENT_TYPES = ['image']
MAX_UPLOAD_SIZE = 5242880  # 5 MB

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
LANGUAGES = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT = False

STATIC_ROOT = os.path.join(BASE_DIR, 'files/static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'files/static'),)
STATIC_URL = '/static/'

COMPRESS_PRECOMPILERS = (
    ('text/scss', 'sass --scss {infile} {outfile}'),
)
COMPRESS_ROOT = os.path.join(BASE_DIR, 'files/static')
# COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'files/media')
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

# META
META_USE_TITLE_TAG = True

# DJANGO-HOSTS
ROOT_HOSTCONF = 'bp.hosts'
DEFAULT_HOST = 'bp'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/main.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_false'],
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/main_debug.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_true'],
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "DEBUG",
        },
    }
}
