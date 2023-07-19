# Django 
# Intro
## Refrence links
- [django Docs.](https://docs.djangoproject.com/en/2.2/)

## TaskManager application 
### End Goal
    A web application in which users on login can add their tasks and tasklists.
### Requirements
1. Template 
    - home
    - dashboard
    - login/Register page
    - Add tasks/Lists
2. databases
3. Form functionality
4. user auth. functionality
5. Deployment

# Learnings / Steps
- make function in `views.py`
- connect `urls.py` with `trelloApp/urls.py` by using include 
- then import views in url and simply connect
    - *first app running*
 # *templates*
- make a template folder in base project directory inside that make another folder(`App_templates`) for storing templates app wise.
- in the App_templates make `base.html` having basic html template.
- using django templates block reusability
```
<head> <title> {% block title %}  {% endblock %}   </title>    </head>
<body>  {% block body %}  {% endblock %}    </body>
```
- then make another html file as required example `home.html`.Inside that do ` {% extends "AppTemplates/base.html" %}` 
and use the blocks as below `{% block title %} any_stuff_we_want {% endblock%}`
- now in `settings.py` in make variable `TEMPLATE_DIR = os.path.join(BASE_DIR,"Templates")` and assign it to `DIR` in `TEMPLATES`
- now finally `views.py` 
```
def home(request):
    return render(request, "AppTemplates/home.html")
```
- in order to provide context to variables used in home.html `{{variable_name}}` put `context = {'variable_name':local_variable}`
- `{% tag_in_template %}` `{% endtag %}`
- `{{variable_in_template}}`
- ### *DataBase*



# DataBase
## main types of DB

### 1. SQL 
- its a relational data base 
- Structured Query Language
- it uses tabular form of storage (stores data in tables)
- provide a query language
- uses B-tree data Structure to store data  ` (learn about it)`

### 2. NoSQL
- example MongoDb
- data stored in json foramt
we will not see this now

> in our project Sqlite3 will be used ie. ` simpler version od sql`

## Operations
 > CRDU
 - retrieving the data efficiently `SELECT`
 - query it effectively
 - insert and change data `UPDATE`
 - adding new data `INSERT`
 - removing the data `DELETE`



 To install [ `sqlite3` ](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-sqlite-on-ubuntu-20-04)

 Further reading about 
 - [operations on table in Sqlite](https://www.sqlitetutorial.net/)
 - [tutorials](https://www.tutorialspoint.com/sqlite/index.htm)

To run sqlite 3 do 
```
sqlite3 file_name.db
```
 then terminal will change to ` sqlite>`
 
 
To check the schema (structure of data base) do 
``` 
.schema
```

## To create a table do 
 ```
CREATE TABLE table_name (
 table data field 1 ,
 table data field 2 ,
 );
 ```
## To insert data into the table
 ```
 INSERT INTO table_name VALUES(
    01,
    "demo table",
    "this table is created on trial basis"
    );
 ```
## To see the table data
```
SELECT * FROM tasks;
```
## To update a table

### Add new column 
`  ALTER TABLE table_name ADD COLUMN column_name column_praticulars ;`

### To insert data in the newly added column
` UPDATE table_name SET column_name = value WHERE id = row.id ;`

### To rename a table
` ALTER TABLE table_name RENAME TO table_new_name ;`

### To update info inside a column
``` 
UPDATE table_name
SET column_name = value
WHERE id = (any_choice)
; 
```

## To join information of two tables

>` SELECT * FROM table_1_name INNER JOIN table_2_name on table_1.id = table_2.id ;`
this command will join the table data and display it 


there are 4 sqlite quories
```
- INNER JOIN
- OUTER JOIN
- LEFT JOIN
- CROSS JOIN
```
## To delete 
``` 
DELETE FROM table_name
WHERE condition like id = 1
;
```
This deletes the whole row with id =1
```
DELETE FROM table_name
WHERE desc_ription LIKE '%trial%'
;
```
This will search for trial in all descr_iptions and delete the row containing trials

___________________________________________________________________________________
___________________________________________________________________________________
___________________________________________________________________________________
___________________________________________________________________________________
> # REFER MOSTLY TO TUTORIALSPOINT DOCUMENTATION FOR SQLITE3 

# Data base MODELS


## keys

| Primary Key | foriegn key |
|--|--|
| its a local unique identifier for everyrow of a table | this is an id or a key word which relates the local/primary key with some other id of any other table |

> in order to describe one to many relation we use foreign keys. Its syntax is
`    extra_column_of_current_table = models.ForeignKey(name_of_another_table, on_delete=models.CASCADE)`

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

checking the sql query fired using python code
`example
name = table_name.objects.all()
name.query.__str__()`
it will give all the queries 
 

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
- The to display our tables in admin portal *first register the models*
- `from . import models` (write in both views.py and admin.py)
- Now to register the models go to `admin.py`>> `admin.site.register(models.table_name_from_models)`

> Now by registering we can add remove modify etc do anything with data base from /admin portal by logging in as superuser



# Django forms
>note irrelevent to heading  while entering datetime values consider this `Exception Value:	
>["'2021-03-02-12-00' value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format."]` as this `.uuuuuu...` enter `00000`
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
this one was from my recent example
```
in >> views.py

def creat_new_list(request):
    
    if request.method == 'POST':

      # getting the data and storing it in the db taskList table
        list_name = request.POST['list_name']
        list_descr = request.POST['list_descr']
         # FIXME: :FIXED >> in below line i was providing the local variable representing the table here but we have to assign values to the actual table name 
         # used in line 5 here table_actual_name.objects.all()
        new_list = taskList(name = list_name , descr = list_descr )
        new_list.save()
        return redirect('index')
    else:    
        return render(request, 'tasks_app_templates/newList.html' )
```

**now this was the general method**
## Django forms
using {{form}} form object that django provides us

- in the app just create forms.py
- from `django.forms import forms`
- like we defined all classes of table in models here we can define a class with the fields we need which inherits the `forms.Form` class
- similar to models we have to define all the feilds we need in our database
- in the template `form.html` just provide a variable  `{{form}}` inside table tag
- now in `views.py` do `from .forms import *`
- then in `creat_function` 
```
Form = TABLE_CLASS_NAME
```
then in context provide `{'form ' : Form}`

> NOTE : we have defined all our fields in models, in order to interract with forms earlier we were doing something like this
```
class Task_form_old(forms.ModelForm):
    name = forms.CharField(label='Your name')#,max_length = 20)
    task_description = forms.CharField( widget= forms.Textarea , label='Your name')
    due_date = forms.DateTimeField()
```
but now and in order to display every field in its correct format we just can do like this >> *our `forms.py` should be like this*
```
from django import forms
from .models import *

class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        <!-- or here u can provide the name of fields as well -->
        fields = ['name', 'date' 'etc']
```
#this magic dunder all method displayes everything provided in the above model as Task which reflect to the Task class in models.py
- now in order to further organise our input fields we can provide **widgets**
```
        widgets = {'due_date': forms.DateTimeInput(attrs={"type":"datetime-local"})}
        #  the above line is providing a right look to date time feild

```

# User Authentication

## Key Points
- django auth
- user table in db
- login/ logout/ register pages/ forms
- Personalised dashboard
- restrict dashboard to logged in users

## Learnings and steps invovled
>**The best practice to impliment user_auth another app should be used to make it global and reusuable**

- creating new app userPages and do all necessary initial steps
- now in `views.py` of `userPages` do `from django.contrib.auth.forms import UserCreationForm` (*TRY AND EXPLORE OTHERS AS WELL*)
- then in `views.py` 
### signup form
 ```
 def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('sigin')
    else:    
        form = UserCreationForm()
    return render(request, 'userPagesTemplates/signup.html', {'form_data':form})
#  in case of is_valid()== false this should return to the same page of signup thats why we are returning outside the else.
```
>* providing the code to avoid much description(understand by looking the example code)*
> here by using this `UserCreationForm` email field is not displayed so
- in order to customize the form creat `forms.py`
- use form class inheritence. we will inherit `UserCreationForm` into our customeform
- then generate the form as earlier and add desired fields
- now there in order to link it with the `model form` using `ORM`
do `import django.contrib.auth.models import User` and `from django.contrib.auth.forms import UserCreationForm `
then assign `model = User`
- then in `views.py` do ` from .forms import * `
-  change `form = UserCreationForm` to `form = signupForm`

### Signin form
- form for getting uesrname, password
- check if user exists in db using `django authenticate` from `django.contrib.auth authenticate`
- if yes, pass the user details with ecery request using `login `method `django.contrib.auth login`
- ***imports needed in `views.py` for signin form***
```
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
```
> note : currently the signup form was made in basic html and will be upgraded to djangoForms soon
```
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user exists :: ?
        user = authenticate(request, username=username, password= password )
        if user is not None:
        # login
            login(request, user)
            return redirect('dashboard')
        else:
            # showing message on invalid credentials
            messages.error(request, "invalid login details")
    return render(request, 'userPagesTemplates/signin.html')
```
> - ***make urls for these pages***
>NOTE: pk django, <int:pk> here pk is short for primary key, which is a unique identifier for each record in a database.

### Signout form
- add a url tag in anchor tag in the template
- assign a url pattern for that url_tag_name
- call the `signout` function in `views.py` 
- in `views.py` `from django.contrib.auth import logout`
- then 
```
def signout(request):
    logout(request)
    return redirect('signin') 
```

## decorators
used to check some given condition to display the views. If condition passes display view else got to provided url.
first in `views.py `do `from django.contrib.auth.decorators import login_required`
then in our case `@login_required(login_url='signin')`
_add this line befoe the view function________________________________________________________________
_________________________________________________________________
_________________________________________________________________
## my personal file structure
(means what am i thinking to connect)
`homePage` >> shows basic info of app and sigIn/signUp button >> 
`signIn/signUp` form page >> 
after login  >> 
`dashboard` on dashboard all the `boards` will be there >>  select board see  `lists `inside it >> select list see ` tasks` inside it 


# using class based views