from .base import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']