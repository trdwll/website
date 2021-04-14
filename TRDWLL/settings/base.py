import os
from os.path import abspath, dirname
from sys import path
# Build paths inside the project like this: os.path.join(SITE_ROOT, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(PROJECT_ROOT)

SITE_ID = 1
INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'localhost',)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.humanize',
    'django.contrib.sitemaps',

    'TRDWLL',
    'blog',
    'experiments',

    # 3rd party
    'django_otp',
    'django_otp.plugins.otp_totp',
    'tinymce',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # 3rd party
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django_otp.middleware.OTPMiddleware',
]

ROOT_URLCONF = 'TRDWLL.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SITE_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'loaders': [
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #     ]),
            # ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'TRDWLL.context_processors.global_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'TRDWLL.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(SITE_ROOT, "static"),
  #  '/var/www/mydomain.com/public_html/static/',
]
# STATIC_ROOT = os.path.join(SITE_ROOT, "static")

# MEDIA_ROOT = '/var/www/mydomain.com/public_html/media/'
# MEDIA_ROOT = os.path.join(SITE_ROOT, "media")
# MEDIA_URL = '/media/'

# FILE_UPLOAD_PERMISSIONS = 0o644

OTP_TOTP_ISSUER = 'TRDWLL'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,insertdatetime,spellchecker,paste,searchreplace,link,image,preview,codesample,table,code,lists,imagetools,autoresize,autolink,emoticons,hr,autosave,charmap,media,toc,help",
    'toolbar1': 'bold italic underline hr charmap insertdatetime | alignleft aligncenter alignright alignjustify | formatselect fontselect fontsizeselect | bullist numlist | outdent indent | table emoticons | link image media toc | codesample | preview code | help',
}

HIGHLIGHT_JS_VERSION = '10.7.2'
HIGHLIGHT_JS_SHA = 'sha512-s+tOYYcC3Jybgr9mVsdAxsRYlGNq4mlAurOrfNuGMQ/SCofNPu92tjE7YRZCsdEtWL1yGkqk15fU/ark206YTg=='
HIGHLIGHT_JS_LIGHT_SHA = 'sha512-11xYl5MU0/AMaYnuBOXDDQdZnl5WGtLVidxqa0XUAXYf6cGnJShNpgtbmB/0MW6ypeev+9Bwj7I/J8wexX8ePw==' # atom-one-light
HIGHLIGHT_JS_DARK_SHA = 'sha512-Fcqyubi5qOvl+yCwSJ+r7lli+CO1eHXMaugsZrnxuU4DVpLYWXTVoHy55+mCb4VZpMgy7PBhV7IiymC0yu9tkQ==' # atom-one-dark
