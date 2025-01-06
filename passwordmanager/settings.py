"""
Django settings for passwordmanager project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os 
from dotenv import load_dotenv
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




 



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY='django-insecure-#8+c11g2j(jk11av20v6r*1jql$p(tpv_@zcrwcv_rspx9dk4o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.243','127.0.0.1','192.168.1.230','marcowolff.me','https://marcowolff.me/',"https://marcowolff.me/","https://passwordmanager-django.onrender.com","https://passwordmanager-django.onrender.*"]
CSRF_TRUSTED_ORIGINS = ['http://marcowolff.me','https://marcowolff.me/','https://marcowolff.*','https://*.marcowolff.me/']
SITE_ID=1

# Application definition
SOCIALACCOUNT_LOGIN_ON_GET=True
ACCOUNT_LOGOUT_ON_GET= True
INSTALLED_APPS = [
    'encrypted_model_fields',
    'dash', 
    'django.contrib.postgres',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'allauth',
    'allauth.account',

    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'passwordmanager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'passwordmanager' / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [ 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend', 
]


WSGI_APPLICATION = 'passwordmanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2', 
#         'NAME': 'mydb', 
#         'USER': 'postgres', 
#         'PASSWORD': '2552', 
#         'HOST': '127.0.0.1', 
#         'PORT': '5432'
#     }
# }

DATABASES ={}
DATABASES['default'] = dj_database_url.parse(
    'postgresql://root:H0pfQsqz6fdNxjlGKWCb9HWxNlchLZ1I@dpg-cttk6j5ds78s73cojsmg-a.ohio-postgres.render.com/passworddb_dfxk',
    conn_max_age=600,
    conn_health_checks=True,
)

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR, os.path.join('static')]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET = os.environ.get("SECRET")

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': CLIENT_ID,
            'secret': SECRET,
            'key': ''
        }
    }
}






AUTH_USER_MODEL="dash.User" 

LOGIN_REDIRECT_URL="/"
LOGOUT_REDIRECT_URL="account_login"