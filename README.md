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

------------------------------------------------------------


### Instalar Entorno Virtual
* python3 -m venv envs/entorno_django

### Activar el Entorno Virtual
* source ./envs/entorno_django/bin/activate

### Ver paquetes instalados en el Entorno Virtual
* pip3 freeze

### Instalar Django Framework
* pip3 install django==3.2.3

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

### Crear Models en la Base de Datos
python3 manage.py makemigrations
python3 manage.py migrate


### Utilerias
1. Verificar qué proceso está usando el puerto
* lsof -i :8000

2. Matar el proceso que está usando el puerto
* kill -9 12345


