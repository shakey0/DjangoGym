# About

[Jump to Key Technologies](#key-technologies)
[Jump to Key Images](#peek-at-the-pages)
[Jump to Key Installation & Setup](#installation--setup)

Welcome to DjangoGym! After learning the fundamentals of Django - Views, URL Patterns, Admin Panel, Templates, Authentication, Django Signals, Class Based Views - I'm now putting it all together with a little project to create a gym web app. In this project I will use these skills I've learnt as well as explore new features such as many-to-many relationships, the use of the is_staff column in the User model, and much more. I have designed this app with a lot of features, buttons and routes, this is because I want to give myself the chance to practice and learn through a good amount of repetition of simply getting things done in Django. Below is the schema I have designed for this project.

<p align="center">
    <img alt="CachingProcess" src="README_images/DjangoGymSchema.png" width="100%"/>
</p>

# Key Technologies

- **Backend:** Python, Django, PostgreSQL
- **Frontend:** JavaScript, SortableJS, Bootstrap, CSS, HTML
- **Deployment:** Docker

# Peek at the Pages

Have a quick look at the pages on the website. These screenshots have been taken while logged in as a staff member, meaning all the buttons to add, edit and delete content are present.

## Homepage
<p align="center">
    <img alt="CachingProcess" src="README_images/homepage.png" width="100%"/>
</p>

## Reordering the Homepage Images
<p align="center">
    <img alt="CachingProcess" src="README_images/homepage_reorder.png" width="100%"/>
</p>

## Classes Page
<p align="center">
    <img alt="CachingProcess" src="README_images/classes.png" width="100%"/>
</p>

## Schedule Page (Of a Specific Class (Kickboxing))
<p align="center">
    <img alt="CachingProcess" src="README_images/specific_class_schedule.png" width="100%"/>
</p>

## Page to Schedule a New Class
<p align="center">
    <img alt="CachingProcess" src="README_images/schedule_class.png" width="100%"/>
</p>

## Staff/Instructors Page
<p align="center">
    <img alt="CachingProcess" src="README_images/staff.png" width="100%"/>
</p>

## Public Instructor Profile
<p align="center">
    <img alt="CachingProcess" src="README_images/public_instructor_profile.png" width="100%"/>
</p>

## Clients Page
<p align="center">
    <img alt="CachingProcess" src="README_images/clients.png" width="100%"/>
</p>

## Page to Add a New Client
<p align="center">
    <img alt="CachingProcess" src="README_images/add_client.png" width="100%"/>
</p>

## Private User Profile
<p align="center">
    <img alt="CachingProcess" src="README_images/private_user_profile.png" width="100%"/>
</p>

# Installation & Setup

Run the following command to clone the repo:
```bash
git clone https://github.com/shakey0/DjangoGym
cd DjangoGym
```

Create your virtual environment:
```bash
pipenv install
pipenv shell
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the following command to create the dev database:
(If you haven't, install and setup PostgreSQL on your machine.)
```bash
createdb DjangoGymData
```

Start the server:
```bash
python manage.py runserver
```