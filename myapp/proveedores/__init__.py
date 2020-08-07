from flask import Blueprint

proveedores = Blueprint('proveedores',__name__, template_folder='templates')

from . import routes