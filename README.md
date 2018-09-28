# Clinic REST

Instrucciones para el REST.

Debe tener instalado PostgreSQL 10.5 o superior con un usuario llamado 'clinic' y contraseña 'clinic', crear una DB llamada 'clinic' y debe ejecutarse en localhost en el puerto por defecto.

$ git clone https://github.com/wxlter97/clinic_rest.git
$ cd clinic_rest
$ source venv/bin/activate
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

En el navegador, dirigirse a 'localhost:8000'.
