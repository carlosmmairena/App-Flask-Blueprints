from flask import Flask
from .proveedores import proveedores

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/config.cfg')
    app.register_blueprint(proveedores)
    return app