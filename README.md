# Bogazici University - Software Engineering, M.Sc. 
## 2021 Fall Semester Software Engineering SWE573 Course Repository

This repo will serve SWE573 course on 2021, Fall semester. \
I will present my researches, code,  project details such as milestones, issues and the results.

Please check out my [Wiki](https://github.com/anilkilickaplan/2021FallSwe573/wiki) for further details.

## Project description
A social knowledge sharing platform where users can create their own events and offers, attend others' and create social networks through the website. \
Attending events and offers are subject to approval by the owner of the event or offer. There will be only time exchange via offers; attendees will give their time equal to event duration (1h, 2h etc.) and the owners will receive an amount equal to event duration.
## How to install this project?


To use this project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/anilkilickaplan/2021FallSwe573```

##System Manual
/*:
- Make sure local system has: postgresql, docker and git
- Create a virtual environment (arbitrary name for virtual env is “myvenv”)
- Go to project directory and in your IDE terminal please write: “source myvenv/bin/activate”
- Install Dependencies $ pip install -r requirements.txt
- Go to the project directory, open ShareClub and open “.env.example.”
- Change file name to “.env”. Update the inside of the document as follows.
-- DJANGO_SECRET_KEY= <your django secret key>
-- DJANGO_DEBUG=True
-- DJANGO_ALLOWED_HOSTS="0.0.0.0"
-- POSTGRES_HOST_AUTH_METHOD= trust
-- DB_ENGINE=django.db.backends.postgresql_psycopg2
-- DB_NAME=devshareclub
-- DB_USER=postgres
-- DB_PASSWORD=q1w2e3
-- DB_HOST=db
-- DB_PORT=5432
-- CORS_ALLOWED_ORIGINS="http://localhost:3000 http://127.0.0.1:3000"
- After step 6, you need to create a database in your local environment. To create a database follow the next step. As mentioned above, make sure that Docker desktop is up and running.
- Create a Database in your local with the following commands (write without $ sign).
-- $ docker-compose up --build
-- $ docker-compose start db 
-- $ docker exec -it core_db bash
-- $ psql -U postgres
-- $ CREATE DATABASE devshareclub;
-- $ /l  (to check if the database is created).
-- After creating a database, write “docker-compose up” in your terminal. Check if the containers are up and running.
-- Create Super User (for Admin page) “python manage.py createsuperuser”
-- Go to your local host port 80 in the browser, 127.0.0.1:80
 */







