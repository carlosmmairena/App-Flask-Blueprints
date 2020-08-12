from flask import Flask
from .proveedores import proveedores
from .productos import productos

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/config.cfg')
    app.register_blueprint(proveedores)
    app.register_blueprint(productos)
    return app