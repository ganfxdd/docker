import os
from os.path import join, dirname
from dotenv import load_dotenv
from celery.schedules import crontab

ENV_PATH = join(dirname(__file__), ".env")
load_dotenv(ENV_PATH)


class CommonConfig(object):
    TESTING = False
    SCHEDULER_API_ENABLED = True

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.urandom(24)

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(**{
        "user": os.environ.get("DB_USER") or "postgres",
        "password": os.environ.get("DB_PASSWORD") or "postgres",
        "host": os.environ.get("DB_HOST") or "localhost",
        "port": os.environ.get("DB_PORT") or 5432,
        "db_name": os.environ.get("DB_NAME") or "app_db_development",
    })

    # Celery
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL") or "redis://localhost:6379",
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND") or "redis://localhost:6379"
    INSTALLED_APPS = ['app']
    CELERYBEAT_SCHEDULE = {}


class DevelopmentConfig(CommonConfig):
    # Flask
    DEBUG = True


class TestingConfig(CommonConfig):
    # Flask
    DEBUG = True


class ProductionConfig(CommonConfig):
    # Flask
    DEBUG = False


_config = {"development": DevelopmentConfig,
           "test": TestingConfig,
           "production": ProductionConfig
           }

Config = _config.get(os.environ.get("FLASK_ENV", "development"))
APP_ROUTE = os.path.dirname(os.path.abspath(__file__))
