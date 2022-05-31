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

## Consola interactiva de python

Consola que permite ejecutar codigo de python, con esta consola tengo acceso al proyecto.

```python
(venv) λ py manage.py shell
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
# importo modelos creados
>>> from polls.models import Choice, Question
# imprimir los registros de question 
>>> Question.objects.all()
<QuerySet []>
# importar libreria timezone
>>> from django.utils import timezone
# Crear registro del modelo question
>>> q = Question(question_text="¿Cual es el mejor curso de platsi?", pub_date=timezone.now())
# Guardar en la bd
>>> q.save()
# verificar que la pregunta creada se haya guardado
>>> q.question_text
'¿Cual es el mejor curso de platzi?'
#traer la pregunta con el pk=1, nota el metodo get trae un solo objeto, para traer varios registros usamos filter
>>> Question.objects.get(pk=1)
<Question: ¿Cual es el mejor curso de platzi?>
```

nota cada vez que nosotros actualizemos o agreguemos algo a los modelos tenemos que ejecutar los comandos

```py
λ py manage.py makemigrations polls
λ py manage.py migrate
```

## Metodo FILTER

El metodo filter se usa para traer varios archivos siguiente el codigo anterior quedaria de esta forma:

```py
# traer registros del año ´presente
>>> Question.objects.filter(pub_date__year=timezone.now().year)
# traer todos los registros que comiencen con ¿Cual
Question.objects.filter(question_text__startswith="¿Cual")
<QuerySet [<Question: ¿Cual es el mejor curso de platsi?>]>
```

## Accediendo al conjunto de respuestas

```py
# obtenemos la pregunta con el id =1
>>> q = Question.objects.get(pk=1)                                 
>>> q                                                              
<Question: ¿Cual es el mejor curso de platsi?> 
# Accedemos a traves de la clave foranea para ver si hay respuestas                    
>>> q.choice_set.all()                                             
<QuerySet []>   
# creamos una respuesta para esa pregunta.                                                   
>>> q.choice_set.create(choice_text="Curso Básico de Python", votes
=0)                                                                
<Choice: Curso Básico de Python>                                   
>>> q.choice_set.count()
3                                                                 
```

# El administrador de Django.

Phyton posee un administrador de datos este administrador nos permite manipular los datos mediante una interfaz grafica.

```py
# comando que nos permite crear un usuario
py manage.py createsuperuser
```

Una vez configurado el usuario y la contraseña vamos a la ruta del proyecto: http://127.0.0.1:8000/admin/login/?next=/admin/

# vistas o views

Arquitectura de Django MTV (Model Templates View)

Django nos permite crear app webs van a estar dividas en dos partes frontend(Templates) y backend(Views). el backend se va a trabajar con un framework de desarrollo por ejemplo flask, Django y FastAPI y el frontend con HTML, CSS Y JS. El backend de Django se usa las views y para el frontend los templates.

las vistas estan construidas en funciones y clases 

## creando vistas.

Configuramos en view.py las vistas

```py
from django.urls import path

from . import views

urlpatterns = [
    #ex: /polls
    path("", views.index, name="index"),
    #ex: /polls/5
    path("<int:question_id>/", views.detail, name="index"),
    #ex: /polls/5/results
    path("<int:question_id>/results/", views.results, name="index"),
    #ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="index")
]
```

## Templates

Polls creamos una carpeta denominada templates/polls

django tiene un lenguaje especial para crear las vistas de nuestra app, que se crea usando los simbolos de la 

```py
{% if latest_question_list  %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}">{{ question.question_text}}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```