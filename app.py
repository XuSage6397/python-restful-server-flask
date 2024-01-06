from flask import Flask
import importlib
import pkgutil

app = Flask(__name__)

for (_, name, _) in pkgutil.iter_modules(['api']):
    module = importlib.import_module(f'api.{name}')
    app.register_blueprint(getattr(module, name))
