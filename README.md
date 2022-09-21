# Django Crud Auth

## Descripción

Codigo base del proyecto Django Crud Auth en el que se aprenderá a instalar y configurar venv, instalar y crear un proyecto utilizando Django, utilizar la base de datos SQL Lite 3, rutas, a configurar y utilizar plantillas de HTML con Python y a realizar el deploy en la plataforma render.com

### En El Caso De Usar virtualenv: Pasos para instalar y utilizar virtualenv

- instalar virtualenv: pip install virtualenv
- crear un entorno virtual: virtualenv venv
- activar el entorno virtual: .\venv\Scripts\activate
- seleccionar el entorno virtual: presionar f1, escribir python select interpreter y elegir la opcion que contiene una estrella

### En El Caso De Usar venv: Pasos para instalar y utilizar venv

- instalar venv: py -m venv venv
- seleccionar el entorno virtual: presionar f1, escribir python select interpreter y elegir la opcion que contiene una estrella

### Comando para instalar Django

- pip install django

### Comando para crear un proyecto de Django

- django-admin startproject nombredelproyecto .

### Comando para ejecutar un servidor de Django

- python manage.py runserver

### Comando para crear una aplicación dentro del proyecto de Django

- python manage.py startapp myapp

### Comando para migrar una base de datos slqlite a DB Browser Sql Lite

- python manage.py migrate

### Comando para crear las migraciones de la aplicación

- python manage.py makemigrations myapp

### Comando para ejecutar el shell de django

- python manage.py shell

### Comando de shell para importar los modelos a la base de datos

- from myapp.models import Project, Task

### Comando de shell para insertar una fila de datos en la base de datos (crea un objeto de una clase y lo ejecuta) POST

- p = Project(name="aplicacion movil")

### Comando para guardar la fila que se inserto en la base de datos (el objeto de la clase)

- p.save()

### Comando para traer una lista de todos los datos de una tabla (lista de objetos de una clase) GET

- Project.objects.all()

### Comando de shell para traer una fila de una tabla (un objeto de una clase) GET

- Project.objects.get(id=1)

### Comando para salir de la consola shell

- exit()

### Comando para crear un dato en una tabla y relacionarla con la tabla principal

- p = Project.objects.get(id=1)

#### Para crear un dato

- p.task_set.create(title="algo")

#### Para consultar todos los datos

- p.task_set.all()

#### Para consultar una tarea

- p.task_set.get(id=1)

### Comando de shell para Buscar todas las filas que empiezen con una palabra mediante un filtro

- Project.objects.filter(name_startswith="aplicacion")

### Comando para crear un super usuario

- python manage.py createsuperuser

## Agregar aplicacion a la carpeta principal

- INSTALLED_APPS = [
  'tasks'
  ]

## Rediccionar al login

- LOGIN_URL = '/signin'

## Desplegar aplicacion en Render.com

### Modulos

- pip install dj-database-url
- pip install psycopg2-binary
- pip install whitenoise[brotli]
- pip install gunicorn
- pip freeze > requirements.txt

### IMPORTS

- import os
- import dj_database_url

### SECRET KEY

- SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

### DEBUG

- DEBUG = 'RENDER' not in os.environ

### HOST

- ALLOWED_HOSTS = []
- RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
- if RENDER_EXTERNAL_HOSTNAME:
  ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

### MIDDLEWARE

- 'whitenoise.middleware.WhiteNoiseMiddleware',

### DATABASES

- DATABASES = {
  'default': dj_database_url.config(
  default='postgresql://postgres:postgres@localhost/postgres',
  conn_max_age=600
  )
  }

### STATIC_URL

- STATIC_URL = '/static/'
- if not DEBUG:
  - STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  - STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
