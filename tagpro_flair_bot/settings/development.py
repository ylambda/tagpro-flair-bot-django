from base import *

STATIC_ROOT = 'static'

try:
    from localsettings import *
except ImportError:
    pass
