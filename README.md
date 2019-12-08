# Stackoverflow-django
work on stackapi with Django

for running the project just write the below link on VS code Terminal:

pipenv shell

python3 manage.py runserver


In this project we have implemented the website which can scrap the newest android question and sorted by the number of votes.
as we can see in the admin page we dont have any question in there
![admin page](https://github.com/sadeghjalalian/Stackoverflow-django/blob/master/Screenshot%202019-12-08%20at%2017.23.40.png)


by passing this url on your browser you can fetch all the data from stackoverflow
http://127.0.0.1:8000/stack/latest

![fetch the newest post](https://github.com/sadeghjalalian/Stackoverflow-django/blob/master/Screenshot%202019-12-08%20at%2017.12.33.png)


the next step is to see the questions in our admin which we can see the list of newest android question sorted by number of voted

![list of questions](https://github.com/sadeghjalalian/Stackoverflow-django/blob/master/Screenshot%202019-12-08%20at%2017.34.00.png)

In the questions we can also see the detail of each questions which contained: Number of views and Number of votes and tags

![question detail](https://github.com/sadeghjalalian/Stackoverflow-django/blob/master/Screenshot%202019-12-08%20at%2017.34.24.png)
