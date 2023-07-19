# Data base MODELS


## keys

| Primary Key | foriegn key |
|--|--|
| its a local unique identifier for everyrow of a table | this is an id or a key word which relates the local/primary key with some other id of any other table |

## Interracting with sql without sqlite terminal using django models

In models.py by defining a class we can control sql queries 
like **className** is the name of table and the *__init__* parameters inside the class act as the table columns
> note : but defining just a class will not work
Here comes the **OOP** concept **Class Inheritance**

> inheritance example `baseClass = vehicles` ==>> `cars, bikes, trucks` are inheritance

defining a simple class
```
class table_name():
    def __init__(self, name, age):
    self.name = name
    self.age = age
```

But in order to use models for sql queries the syntax little differs
```
class table_name(models.Model):
    column_name = models.CharField(max_length = 50)

```
- Here `models.Model` is the inheritance of class model in class table_name. 
- we are using the content of `models class` inside `table_name`

> **ORM** - Object Relational Mapper || by this we maps our tbale to sql

## running the models
- to run first go to `settings.py` of the project in `installed_apps` add name of the app you are in, 
- then `python3 manage.py makemigrations`
    (All changes will be done)
- now to run do `python3 manage.py migrate`
 > by this in data base the tables will be created u can check using `.schema tables` in `sqlite` shell


## inserting data into tables created using models
- for this we can use the django provided shell
- `python3 manage.py shell`
- then `from app_name.models import *`
- Now to check the data run `class_name.object.all()`


    > note : while using django shell to insert values in tables
    > the first value we provide goes to tge id and the second value goes to the first attribute
    > ```
    > 
    >In [12]: task = Task("migrations","learn dja
    >    ...: ngo models and migrations" '01-03-2
    >    ...: 1','2-3-21')
    
    **Output**
    >In [14]: task.name
    >Out[14]: 'learn django models and >migrations01-03-21'
    >
    >In [15]: task.descr
    >Out[15]: '2-3-21'
    >
    >In [16]: task.due_date
    >
    >In [17]: task.id
    >Out[17]: 'migrations'
    >```

- By doing above actions the data is just generated not saved
- in order to avoid the above probel we can do
```

In [33]: task3 = Task(name = "some 
    ...: stuff", descr = "bored to 
    ...: write it now", time_stamp
    ...: = timezone.now(), due_date
    ...:  = timezone.now())

```
do `tas2.save()`

# MIGRATIONS
## Changing models(updating schema of existing tables without disturbing the existing data)

Django provides general scripts whcih identifies the difference in old schema and new schema and generates a **migration script** 
- **steps**  
- make changes in models 
- remove table, rename add etc 
- Provide some sort of default value 
- make migrations  
- run migrations 
                

`python3 manage.py makemigrations` >> makes the migration script

`python3 manage.py migrate`  >> runs the migration script

# Admin k sath hushari
- In order to get admin privlgs
`puthon3 manage.py createsuperuser`
- The to display our tables in admin portal *first regerter the models*
- `from . import models` 
- Now to regester the models go to `admin.py`>> `admin.site.regester(models.table_name_from_models)`

> Now by registering we can add remove modify etc do anything with data base from /admin portal by logging in as superuser



# Django forms

## Requesting data from data base in views.py to render
- For this >> `from .models import *`
- Then simply assign it to dictionaries or lists as we weere doing earlier
- Pass it to the template by context
 
# steps involved in forms
>making a form for user(other than admin) to add  new lists in the db

1. creat an html form with post method
>   if we directly use post method in html form there will be an *err 403* *forbidden* `CSRF verification failed`
    > **CRSF** >> *Cross site request- forgery protection* a security level provided by django 
    > This is just like preventing other user to post the request on behalf of your identity.[refer further docs](https://docs.djangoproject.com/en/3.1/ref/csrf/)
> To avoid this err we have to add `{% csrf_token %}` inside the form tag of html file 

2. Now in `views.py` compare the `request.method == 'POST'` then assign values to variables by doing 
```
var = request.POST('name_of_field_used_in_html_file')
ran_var = table_name_as_in_our_db    (column_name = var)
ran_var.save()

#then finally 

return redirect('index_page')
```

**now this was the general method**
## Django forms
using {{form}} form object that django provides us

- in the app just create forms.py
- from `django.forms import forms`
- like we defined all classes of table in models here we can define a class with the fields we need which inherits the `forms.Form` class

