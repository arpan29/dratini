# README #

This README would normally document whatever steps are necessary to get your application up and running.
This is a Django Boilerplate Quickstart Kit to boot up any Django microservice quickly.

### Dependencies ###

* Python 3.x
* PostGreSQL 11.x


### Getting Started ###

* Create a user for postgres : "createuser kamar-taj --pwprompt --superuser"
* Set password for the user : <DB_PASSWORD>
* Create a db for the application : "createdb dratini"


### Virtual Environment Setup ###

* Setup cauldron virtualenv : "virtualenv -p python3.6 dratini"
* Move to virtualenv and activate its environment


### Dependency Setup ###

* Install requirements: "pip install -r requirements.txt".
* In settings.py, change <DB_PASSWORD>
* Run migrations: "python manage.py migrate"
* Create superuser: "python manage.py createsuperuser"
