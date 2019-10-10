from flask import Flask
from flask_cors import CORS
from celery import Celery
from app.config import Config
from app.database import init_db
import os


def create_celery(_app: Flask) -> Celery:
    """
    Celeryの初期化
    """
    _celery: Celery = Celery(
        _app.import_name,
        backend=_app.config['CELERY_RESULT_BACKEND'],
        broker=_app.config['CELERY_BROKER_URL'],
        include=['app.tasks']
    )
    _celery.conf.update(_app.config)

    class ContextTask(_celery.Task):
        def __call__(self, *args, **kwargs):
            with _app.app_context():
                return self.run(*args, **kwargs)

    _celery.Task = ContextTask
    return _celery


def create_app() -> Flask:
    """
    Flaskアプリケーションの初期化
    """
    _app: Flask = Flask(__name__)
    CORS(_app)
    # Flaskのconfigが 設定ファイルを読み込む処理
    _app.config.from_object(Config)

    # DBセッションの暗号化のため
    _app.secret_key = os.urandom(24)
    # DB初期化
    init_db(_app)
    return _app

# For external
app: Flask = create_app()
celery: Celery = create_celery(app)
