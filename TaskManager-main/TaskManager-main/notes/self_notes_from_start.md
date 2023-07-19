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

# Django models
> Helps in interracting with databases
> ORM object relational mapping
