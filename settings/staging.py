from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_BXMhGZbzUnHrO4wR2QDrLSN1')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_L2u1PAnN0QLTVcbLRes1qB2W')

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://velabri.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'edward.stack@mail.com'

SITE_URL = 'https://velabri.herokuapp.com/'
ALLOWED_HOSTS.append('velabri.herokuapp.com/')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
