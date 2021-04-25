# unidos-por - Readme :v:

Este proyecto esta en su etapa de inicio, permitirá visualizar todos los eventos para recaudaciones de fondos (Polladas, hamburgueseadas, etc).

A la fecha cuenta con dos templates básicos y en desarrollo.

# Sobre el proyecto :eyes:

Se trata de un sitio de eventos que sirven para recaudar fondos para una actividad en específica.

Cualquier persona puede registrar su actividad, proporcionando datos como: Fecha y hora, dirección, costo, entre otros.

## Pre-requisitos :clipboard:

[requirements.txt](https://github.com/gildarey/unidos-por/)

## Instalación en el entorno local :dvd:

### Clonar el repositorio:

```
$ git clone https://github.com/gildarey/unidos-por.git
$ cd unidos-por
```

### Cree un archivo .env con los correspondientes datos

```
LOCAL=True
SECRET_KEY=yoursecretkey
GOOGLE_MAPS_API_KEY=yourgooglemapskey
USER_MAIL=yourusermail
USER_MAIL_PASSWORD=yourpassword
```

#### Cree un entorno virtual para instalar dependencias y actívelo:

```
$ virtualenv myenv
$ source myenv/bin/activate
```

o

```
$ python3 -m venv myenv
$ source myenv/bin/activate
```

#### Luego instale las dependencias:

```
(myenv)$ pip install --upgrade pip
(myenv)$ pip install -r requirements.txt
```

#### Una vez que haya terminado de descargar las dependencias, correr el server:

```
(myenv)$ python manage.py migrate
(myenv)$ python manage.py runserver
```

#### Y navegue hasta http://127.0.0.1:8000/

## Deployar en [Heroku](https://devcenter.heroku.com/articles/heroku-postgresql) :rocket:

### En la consola de Heroku en la parte de variables de configuracion [info](https://devcenter.heroku.com/articles/config-vars) , puede agregar las siguientes configuraciones

```
SECRET_KEY=yoursecretkey
GOOGLE_MAPS_API_KEY=yourgooglemapskey
DATABASE_URL=yourdatabaseurl
AWS_ACCESS_KEY_ID=yourawskey
AWS_SECRET_ACCESS_KEY=yourawskey
AWS_STORAGE_BUCKET_NAME=yourawskey
USER_MAIL=yourusermail
USER_MAIL_PASSWORD=yourpassword
```

### Luego desde su consola:

```
(myenv)$ heroku login # inicie sesion en su cuenta de heroku
(myenv)$ heroku create yourappname
(myenv)$ heroku git:remote -a yourappname
(myenv)$ heroku addons:create heroku-postgresql:<PLAN_NAME>  # Por ejemplo, hobby-dev
(myenv)$ git push heroku master:master
(myenv)$ heroku run python manage.py migrate
```

## Contribuciones :raised_hands:

[Gilda Rey](https://github.com/gildarey/) - Trabajo inicial

## Versiones :arrows_clockwise:

## Autores

[Gilda Rey](https://github.com/gildarey/) - Trabajo inicial

Consulte también la lista de colaboradores que participaron en este proyecto.
