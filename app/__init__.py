from app.application import app, celery
import importlib


# View, Modelのロード(PEP8対策)
importlib.import_module("app.models")
importlib.import_module("app.views")

