# App-Flask-Blueprints
Estructura básica de un proyecto web con Flask Micro-Framework, con Blueprints implementado para la modularización de rutas.  
Este proyecto solo contiene 2 archivos .html en los módulos Productos y Proveedor, pero sin ningún tipo de diseño GUI en particular.  
  
## Estructura de directorios
  
myapp/  
├── config  
│   ├── config.cfg  
│   └── test.py  
├── static   
|   ├── css  
|   │   └── loquesea.css  
|   └── js  
|       └── loquesea.js  
├── __init__.py  
├── productos  
│   ├── __init__.py  
│   ├── routes.py  
│   ├── static   
│   └── templates  
│       ├── formulario-producto.html  
│       └── productos.html  
├── proveedores  
   ├── __init__.py  
   ├── models.py  
   ├── routes.py  
   └── templates  
        ├── Formulario.html  
        └── Proveedores.html     
 
----  

## Despliegue en Apache2  
 
Esta vez vamos a crear una [WSGI](https://docs.appseed.us/content/what-is/wsgi) de apache para desplegar esta aplicación, muestro a continuación todos los pasos para poder replicarlo por tu cuenta.   
Esto es desplegado en Ubuntu 18.04, pero puede funcionar en otra distribución y versión, mientras se tenga los siguientes **requerimientos**:  
 
 1. Python3.6 o superior
 2. python3.6-venv o superior
 3. Apache2
 4. El paquete libapache2-mod-wsgi-py3  

---

### Preparación del servidor (Ubuntu)  
 
#### 1 - Actualiza los repositorios  
Ejecuta: `$ sudo apt-get update`   

#### 2 - Instala python3 y python3-venv  
Ejecuta: `$ sudo apt-get install python3 python3-venv`  

#### 3 - Instala Apache2 y libapache2-mod-wsgi-py3  
Ejecuta: `$ sudo apt-get install apache2 libapache2-mod-wsgi-py3`  

#### 4 - Incia el servicio de apache  
Ejecuta: `$ sudo /etc/init.d/apache2 start`  
Ejecuta: `$ sudo /etc/init.d/apache2 status`  

  
---
### Configuración de Apache2 y nuestra aplicación  

#### 1 - Crea un entorno virtual  
Ejecuta: `$ python3 -m vevn env`  

#### 2 - Activa el entorno virtual e instala las dependencias  
Activar el entorno, ejecuta: `$ source env/bin/activate`  
Instalar dependencias, ejecuta: `$ pip3 install -r requirements.txt`  

#### 3 - Cambia el propietario de los archivos
Ejecuta: `$ chown www-data.www-data App-Flask-Blueprints/ -R`

#### 4 - Crea el VirtualHost de Apache
En este caso te he dejado un archivo ya preparado ([App-Flask.conf](https://github.com/carlosmmairena/App-Flask-Blueprints/blob/master/App-Flask.conf)), el cual ya tiene una configuración inicial.  
Copialo en la ruta `/etc/apache2/sites-available/`.  
Ejecuta: `$ sudo cp App-Flask.conf /etc/apache2/sites-available/000-default.conf`  

#### 5 - Modifica el path de tu proyecto en el VirtualHost  
Este archivo ([App-Flask.conf](https://github.com/carlosmmairena/App-Flask-Blueprints/blob/master/App-Flask.conf)) lo he dejado con un path, posiblemente distinto al tuyo, por lo que debes abrir el archivo `/etc/apache2/sites-available/000-default.conf` y modificarlo.  
Ejecuta: `$ sudo vim /etc/apache2/sites-available/000-default.conf`  

#### 6 - Reinicia el servicio de Apache2  
Ejecuta: `$ sudo /etc/init.d/apache2 restart`  
Ejecuta: `$ sudo /etc/init.d/apache2 status`  

---  

¡Listo! Ya tienes desplegada tu aplicación escrita con Flask en Apache2, utilizando la interfaz [WSGI](https://docs.appseed.us/content/what-is/wsgi).  
*Esta configuración puede funcionar en DJango, inténtalo.*  

  
------------------------------  
Desarrollado por: @carlosmmairena  
Instagram: https://www.instagram.com/carlosmmairena/  
StackShare: https://stackshare.io/carlosmmairena  
