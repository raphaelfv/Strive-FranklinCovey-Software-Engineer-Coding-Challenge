## Installation

* Create a virtual env

```
python3 -m venv myvenv
```

* Install dependencies 

```
. myvenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py migrate --run-syncdb
```

* Create user for testing

```
python manage.py createsuperuser
```

## Use

* Development environment 

```
. myvenv/bin/activate
python manage.py runserver
```

In a web browser, you can access 127.0.0.1:8000

* Including data

You can access 127.0.0.1:8000/admin to include new Quizzes. One initial quiz is already set by admin.py for use in the MVP. 
