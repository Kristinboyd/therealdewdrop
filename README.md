Commands for Startup
python3 manage.py makemigrations 
python3 manage.py migrate 
python3 manage.py runserver 
python3 manage.py creatsuperuser 
pip install coverage 
coverage run --omit='*/venv/*' manage.py test 
coverage html 

pip install djangorestframework 

Endpoints Examples:
User filters Products based on dry skin 
http://127.0.0.1:8000//products/filter/user/?treatment_type=DRY

Individual Product:
http://127.0.0.1:8000//products/1

User Profile
http://127.0.0.1:8000/profile/

User adds the product to the Profile
http://127.0.0.1:8000/products/add-to-profile/user/?product_name=Drunk%20Elephant

Admin to add products
http://127.0.0.1:8000/products/add-product 

pip install django-filter





STEPS FOR NEW POSTGRES -------------------------------------------------------->
$ pip install psycopg2
$ psql -U postgres
$ CREATE DATABASE therealdewdrop;

add this into your settings.py file and comment out the following: 

 <!-- DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
} -->

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'therealdewdrop',

        'USER': 'postgres',

        'PASSWORD': 'postgres',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}

then: 
$ pip freeze > requirements.txt
$ python manage.py migrate
$ pip install django-crispy-forms
$ python manage.py runserver

