import os

from fittrack_project.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'kpm*6ijt=j*i9jh!f87^)n_wgz^)v!e_#pa1ff%_^0^j4f4oy3'


