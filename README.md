# q4ghostpost
This assessment was completed during the 4th quarter of the year that I studied at Kenzie


This assessment has a React front-end and a Django back-end.

You will need two terminals open to run this program after you clone this repo down onto your machine. 

You will also need to have Poetry installed on your machine. 

***
In terminal 1:

CD into "react-frontend"

Run "npm i" to install dependencies.

Then "npm start" to spin up the front end server on localhost:3000
***


***
In terminal 2:

CD into "django-backend"

Run "poetry install" to install dependencies.

Run "poetry shell" to activate the virtual environment

Run "python manage.py generate" to generate a secret key and overwrite the dummy string in the .env file. This command also will unstage the .env from git, ensure that the gitignore file is added to the stage, and migrate the data. After that is done, fake data is generated with a bulk create command for demonstration of the app

Then "python manage.py runserver" to spin up the back end server
***

After that, you can post "ghostposts", view different pages to see them filtered accordingly, and up vote or down vote them