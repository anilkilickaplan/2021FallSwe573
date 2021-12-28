# Bogazici University - Software Engineering, M.Sc. 
## 2021 Fall Semester Software Engineering SWE573 Course Repository

This repo will serve SWE573 course on 2021, Fall semester. \
I will present my researches, code,  project details such as milestones, issues and the results.

Please check out my [Wiki](https://github.com/anilkilickaplan/2021FallSwe573/wiki) for further details.

## Project description
A social knowledge sharing platform where users can create their own events and offers, attend others' and create social networks through the website. \
Attending events and offers are subject to approval by the owner of the event or offer. There will be only time exchange via offers; attendees will give their time equal to event duration (1h, 2h etc.) and the owners will receive an amount equal to event duration.

<h2> How to install this project?</h2>

Make sure local system has: postgresql, docker and git

Install Dependencies pip install -r requirements.txt \
Create a Database in your local\

<ul>
  <li>docker-compose run db -d</li>
  <li>docker exec -it core_db bash</li>
  <li>psql -U postgres</li>
  <li>CREATE DATABASE </li>
</ul>

Create Super User (for Admin page) python manage.py createsuperuser \
Run Server python manage.py runserver 

<h2> How to use the product? </h2>
TBD



