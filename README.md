# Clinic REST

Instrucciones para el REST.

Debe tener instalado python3, python3-pip, python-virtualenv, PostgreSQL 10.5 o superior con un usuario llamado 'clinic' y contraseña 'clinic', crear una DB llamada 'clinic' y debe ejecutarse en localhost en el puerto por defecto.

$ git clone https://github.com/wxlter97/clinic_rest.git

$ cd clinic_rest

$ virtualenv venv

$ source venv/bin/activate

$ pip install requirements.txt

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver

En el navegador, dirigirse a 'localhost:8000'.
