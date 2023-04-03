# foreCast
This app was my final year project which is a platform meant to assist farmer get weather forecast, from weatherapi and use the information 
to make decision on best crop to grow during a certain period


##Modules
staff
results and
finances.
It currently doesn't allow students/staff to login.

Demo
Demo stopped working on https://forecas.herokuapp.com since Heroku has stopped their free version.


Install in PostgreSQL and make sure python is installed on the system

git clone https://github.com/danielskiptoo/foreCast.git
Then

cd foreCast
Run

pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server
Then locate http://172.0.0.1:8000

