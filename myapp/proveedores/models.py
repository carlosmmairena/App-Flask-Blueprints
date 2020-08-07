class Proveedor():
    """
        En realidad esta clase debería heredar de un objeto modelo de SQLAlchemy
    """
    __nombre = str
    __direccion = str
    __cedula_juridica = str

    def __init__(self, nombre, direccion, cedula):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__cedula_juridica = cedula

    def __str__(self):
        return ('Nombre: '+ self.__nombre + '\nDirección: '+
            self.__direccion + '\nCédula Jurídica: '+
            self.__cedula_juridica)

