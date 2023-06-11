 @echo off
call %~dp0\.venv\Scripts\activate
cd %~dp0\
python manage.py runserver
cmd /k 
