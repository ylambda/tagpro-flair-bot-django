from base import *

# Static asset configuration
STATIC_ROOT = 'static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


try:
    from localsettings import *
except ImportError:
    pass
