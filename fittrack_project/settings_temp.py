import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'fittrack'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': '',
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://caching:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "fittrack"
    }
}

# Cache time to live
CACHE_TTL = 60 * 15

SECRET_KEY = 'kpm*6ijt=j*i9jh!f87^)n_wgz^)v!e_#pa1ff%_^0^j4f4oy3'


