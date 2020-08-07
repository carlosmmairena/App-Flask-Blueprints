from flask import render_template
from . import proveedores

@proveedores.route('/proveedores', methods=['GET', 'POST'])
def mostrar_proveedores():
    return render_template('Proveedores.html')

@proveedores.route('/registrar-proveedor', methods=['GET', 'POST'])
def registrar_proveedores():
    return render_template('Formulario.html')
