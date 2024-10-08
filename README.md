## README


### Instalar Entorno Virtual Pyenv
* pyenv install 3.12.4

* pyenv virtualenv 3.12.4 env_django_3.2.3

* pyenv activate env_django_3.2.3

### Es necesario para instalar django 3.2.3
* python -m pip install --upgrade pip
* pip install setuptools
* pip install distlib

### Instalar Django 3.2.3
* pip3 install django==3.2.3

### Instalar Django Rest Framework 3.12.4
* pip3 install djangorestframework==3.12.4

------------------------------------------------------------

### Instalar Entorno Virtual venv
* python3 -m venv envs/entorno_django

### Activar el Entorno Virtual
* source ./envs/entorno_django/bin/activate

### Ver paquetes instalados en el Entorno Virtual
* pip3 freeze

### Instalar Django Framework
* pip3 install django==3.2.3

### Instalar Django Rest Framework 3.12.4
* pip3 install djangorestframework==3.12.4

------------------------------------------------------------

### Crear Proyecto Django
* django-admin startproject my_blog

### Ayuda Comando Django
* python3 manage.py help

### Levantar Proyecto Django
* python3 manage.py runserver

### Crear super usuario en Django
* python3 manage.py createsuperuser

### Crear Aplicación Django
* python3 manage.py startapp posts

* python3 manage.py startapp user

------------------------------------------------------------

### Crear Models en la Base de Datos
* python3 manage.py makemigrations
* python3 manage.py migrate

### Crear Documentación
* pip3 install drf-yasg==1.20.0
 
### Generar staticos
* python3 manage.py collectstatic

### JWT Autentificación
* pip3 install djangorestframework-simplejwt==4.7.1

### Instalar driver para PostgreSQL

* brew install postgresql libpq libpq-dev libq-devel

* pip3 install psycopg2-binary==2.8.6

* pip3 install psycopg2


------------------------------------------------------------



# Documentación

* Django Rest Framework
https://www.django-rest-framework.org/

* ViewSet
https://www.django-rest-framework.org/api-guide/viewsets/#viewsets

* ModelViewSet:
https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset

* drf-yasg
https://pypi.org/project/drf-yasg/

* drf-yasg - Yet another Swagger generator
https://drf-yasg.readthedocs.io/en/stable/readme.html#usage

* psycopg2 Driver para PostgresSQL
https://pypi.org/project/psycopg2/

------------------------------------------------------------

### Utilerias
* Puerto Ocupado 

1. Verificar qué proceso está usando el puerto
* lsof -i :8000

2. Matar el proceso que está usando el puerto
* kill -9 12345


