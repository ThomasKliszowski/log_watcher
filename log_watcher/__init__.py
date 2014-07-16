import log_watcher
import imp
import logging.config
import os

# -----------------------------------------------------------------------------
# Set app settings to log_watcher.settings endpoint

SETTINGS_PATH = os.environ.get('SETTINGS_PATH', '/opt/log_watcher/settings.py')
if not hasattr(log_watcher, 'settings'):
    log_watcher.settings = imp.load_source(
        'log_watcher.settings',
        SETTINGS_PATH)
from log_watcher import settings


settings.CURRENT_DIR = os.path.dirname(__file__)
settings.VERSION = open(os.path.join(
    settings.CURRENT_DIR,
    '..',
    'VERSION.txt')
).read()

# -----------------------------------------------------------------------------
# Configure logging

settings.LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}

# Handle sentry conf
if hasattr(settings, 'SENTRY_DSN'):
    settings.LOGGING['handlers']['sentry'] = {
        'level': 'ERROR',
        'class': 'raven.handlers.logging.SentryHandler',
        'dsn': settings.SENTRY_DSN,
    }
    settings.LOGGING['loggers']['']['handlers'].append('sentry')

logging.config.dictConfig(settings.LOGGING)
