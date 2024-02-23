import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*lf^y=$n-hw*^vsdsadasdqq15oq$5y79qcs^^x-eiu%0u&66t'

DEBUG = True

ALLOWED_HOSTS = []

STATIC_DIR = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIR = [STATIC_DIR]



STATIC_DIR = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [STATIC_DIR]
