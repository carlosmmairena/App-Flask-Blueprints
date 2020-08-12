from flask import render_template
from . import productos

@productos.route('/productos', methods=['GET', 'POST'])
def mostrar_productos():
    return render_template('productos.html')

@productos.route('/guardar-producto', methods=['GET', 'POST'])
def guardar_producto():
    return render_template('formulario-producto.html')