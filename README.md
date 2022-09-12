# Introduction

This project was built to fulfil the assignment given for evaluation.

# Task Manager
The goal of this project is to create a simple Task Manager in which a user can manage their tasks.

# Getting Started

First clone the repository from GitHub and switch to the new directory:

    $ git clone git@github.com:namansingh3502/task-manager.git

## Installation and Setup Instructions for Django

    $ cd task-manager
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt

You can now run the development server:

    $ python manage.py runserver

## URL endpoints

login  : http://127.0.0.1:8000/auth/token/login/

logout : http://127.0.0.1:8000/auth/token/logout/

task-list  : http://127.0.0.1:8000/api/task-list/

task-details  : http://127.0.0.1:8000/api/task-detail/<task_id>/

task-create  : http://127.0.0.1:8000/api/task-create/

task-update  : http://127.0.0.1:8000/api/task-update/<task_id>/

task-delete  : http://127.0.0.1:8000/api/task-delete/<task_id>/