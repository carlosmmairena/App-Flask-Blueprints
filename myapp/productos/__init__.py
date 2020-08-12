from flask import Blueprint

productos = Blueprint('productos',__name__, template_folder='templates')

from . import routes