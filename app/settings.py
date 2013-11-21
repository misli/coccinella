# Django settings for coccinella project.
# encoding: utf-8

import os
from os.path import dirname, join, realpath
from django.utils.translation import ugettext_lazy as _

PROJECT_PATH = dirname(dirname(realpath(__file__)))

DEBUG = 'DEBUG' in os.environ and os.environ['DEBUG'] and True or False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jakub Dorňák', 'jakub.dornak@misli.cz'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'coccinella',                 # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'coccinella',
        'PASSWORD': 'fb6c3ef18149a6739ffc3b3535b40194',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['coccinella.cz']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cs'

LOCALE_PATHS = (
    join(PROJECT_PATH, 'conf', 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = join(PROJECT_PATH, 'htdocs', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = join(PROJECT_PATH, 'htdocs', 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+@v7=g9scta^gk6d^s3-ll)xhzc)0nz-1e4u1e4dnj$p$-q69k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    #'cms.middleware.language.LanguageCookieMiddleware',
    'misli.middleware.SecureAdminMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # BEGIN cms
    'djangocms_text_ckeditor',
    'cms',
    'cms.stacks',
    'mptt',
    'menus',
    'south',
    'sekizai',
    #'djangocms_admin_style',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    #'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.video',
    'cms.plugins.inherit',
    #'cmsplugin_text',
    # END cms
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'photologue',
    'cmsplugin_photologue',
    'tagging',
    'misli',
    'sortedm2m',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

APPEND_SLASH = True

LANGUAGES = (
    ('cs', 'Čeština'),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'cs',
            'name': _('Czech'),
        },
    ],
    'default': {
        'public': True,
        'fallbacks': ['cs'],
        'hide_untranslated': True,
        'redirect_on_fallback': True,
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'misli.context_processors.misli',
)

CMS_TEMPLATES = (
    ('default.html', _('Default')),
)

CMS_PLACEHOLDER_CONF = {
    'content': {
#        'plugins': ['TextPlugin', 'PicturePlugin'],
#        'text_only_plugins': ['LinkPlugin']
#        'extra_context': {'width':640},
        'name': _('Content'),
#        'language_fallback': True,
#        'child_classes': {
#            'TextPlugin': ['PicturePlugin', 'LinkPlugin'],
#        },
#        'parent_classes': {
#            'LinkPlugin': ['TextPlugin', 'StackPlugin'],
#        }
    },
}

CMS_PERMISSION = False

# Show the publication date field in the admin, allows for future dating
# Changing this from True to False could cause some weirdness.  If that is required,
# you should update your database to correct any future dated pages
CMS_SHOW_START_DATE = True

# Show the publication end date field in the admin, allows for page expiration
# Changing this from True to False could cause some weirdness.  If that is required,
# you should update your database and null any pages with publication_end_date set.
CMS_SHOW_END_DATE = True

# Whether the user can overwrite the url of a page
CMS_URL_OVERWRITE = True

# Allow to overwrite the menu title
CMS_MENU_TITLE_OVERWRITE = True

# Are redirects activated?
CMS_REDIRECTS = True

# Allow the description, title and keywords meta tags to be edited from the
# admin
CMS_SEO_FIELDS = True

# Wheter the cms has a softroot functionionality
CMS_SOFTROOT = False

# Path (relative to MEDIA_ROOT/MEDIA_URL) to directory for storing page-scope files.
CMS_PAGE_MEDIA_PATH = 'pages/'
CMS_MEDIA_URL = MEDIA_URL

# Enable non-cms placeholder frontend editing
PLACEHOLDER_FRONTEND_EDITING = True

# jquery settings
JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'

# Use SortedManyToManyField
PHOTOLOGUE_USE_SORTEDM2M = True

CMSPLUGIN_PHOTOLOGUE_PHOTO_TEMPLATES = (('coccinella', _('coccinella')),)
CMSPLUGIN_PHOTOLOGUE_GALLERY_TEMPLATES = (('coccinella', _('coccinella')),)

# security settings
SECURE_PROXY_SSL_HEADER = ('SECURE', 'true')
SESSION_COOKIE_SECURE = not DEBUG
