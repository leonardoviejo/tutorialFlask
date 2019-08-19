import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f9155d31-b132-4a70-99bd-f075f16e0d19'