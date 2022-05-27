# conceptos-basico-django
Python Django Create, read, update and delete (CRUD)

**¿Qués es django?:** Uno de los frameworks más populares para crear web apps

## Instalación de Django

Creación de entorno virtual 

```
py -m venv venv
```

Activar el entorno virtual

```
.\venv\Scripts\activate
```

Instalación de Django

```
pip install django
```

Crear directorio de carpetas con Django

```
django-admin startproject premiosApp
```
Para correr el servidor nos dirigimos a premiosApp y corremos el comando:

```
py manage.py runserver
```

# Configuración de proyectos a trabajar

## Observación 

**proyecto:** Un proyecto en Django es un conjunto de aplicaciones Ejm: instagram aplicaciones que lo conforman
- Feed
- Stories
- messages

Crear aplicacion dentro de premiosApp 

```
py manage.py startapp polls
```
## archivo setting.py

Databases: contiene la informacion de la bd 
- **Engine:** motor de la base de datos
- **name:** nombre o dirección de la bd
- **TIME_ZONE:** Zona horaria a partir de la cual funciona nuestro proyecto.
- **INSTALLED_APPS:** Aplicaciones instaladas en el proyecto.

## ¿Qué es un ORM? ¿Qué es un modelo?

**¿Qué es un ORM?:** **Object Relational Mapping** nos explica como relacionar la estructura de una base de datos con la programación orientada a objetos.

**Modelo:** representación de una tabla , donde cada una de las columnas contiene el tipo de datos ejmp (string, int ...). 

## Diagrama de Entidad relacional

ORM como usarlo en Django:

al generar los documentos de la carpeta polls se crea en uno de los archivos un models.py aqui crearemos nuestros modelos.

```python
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
Una vez listos los modelos de nuestra app procedemos a ejecutar el comando :

```
\Users\Yohana\Github\conceptos-basico-django\premiosApp(tutorial-2-models)
λ py manage.py makemigrations polls
λ py manage.py migrate
```

creamos el mapeo de la base de datos tomando los modelos y transformandolos en tablas sqlite3.

**link importantes**
Configuracion del campo time_zone 
> https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

