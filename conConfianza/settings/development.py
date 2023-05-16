from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost']

# Database and Channel Layer for ASGI. 

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}
