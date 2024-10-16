# Proyecto Blog - Django Rest Framework

------------------------------------------------------------
## Crear Proyecto

* django-admin startproject blog

## Crear App User 

* python3 manage.py startapp users

* python3 manage.py startapp categories

* python3 manage.py startapp posts

### Crear Models en la Base de Datos
* python3 manage.py makemigrations
* python3 manage.py migrate

### Crear Documentación
* pip3 install drf-yasg==1.20.0

### Generar staticos
* python3 manage.py collectstatic

### Subir Imágenes
* pip3 install Pillow==10.4.0

### Servidor a instalar
* pip3 install gunicorn
