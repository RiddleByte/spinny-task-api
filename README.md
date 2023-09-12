# Spinny Task - Cuboid Box Inventory Management API

## General Information
This API service allows you to perform CRUD (Create, Read, Update, Delete) operations on cuboid boxes in a store. It also enforces various permissions, filters, and configuration settings. It addresses the need for efficient inventory management in a store, ensuring data accuracy, user access control, and adherence to specific constraints. It streamlines the process of adding, updating, viewing, and deleting boxes while maintaining data integrity and enforcing business rules.

## Technologies Used

- Django: A high-level Python web framework.
- Python 3: The programming language used for development.
- MySQL: The relational database system for storing box and user data.
- Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs in Django.

## Setup

### Prerequisites

- Python >= 3.11.5
- Django >= 4.2.5
- MySQL database

### Getting Started

1. Clone the Repository:
- git clone https://github.com/ashushm1/spinny-task-api


2. Create a Virtual Environment:
- python -m venv venv
- source venv/bin/activate


3. Install Dependencies: 
- pip install -r requirements.txt


4. Database Configuration:

- Create a MySQL database.
- Create a `dotenv` folder and add a local file in the folder without any extension.
- Update the database settings in the local file to match your database configuration.

5. Apply Migrations:
- python manage.py makemigrations
- python manage.py migrate


6. Create a Superuser (for initial access to the admin panel):
- python manage.py createsuperuser


7. Run the Server:
- python manage.py runserver


## Features

- Create, Read, Update, and Delete operations for cuboid boxes.
- User authentication and permissions to control data access.
- Data filtering options.
- Configuration settings for business rules and data validation.

## Purpose

The purpose of the Spinny Task project is to streamline the management of cuboid boxes in a store. It aims to:

- Maintain data accuracy.
- Enforce business rules.
- Provide a user-friendly interface for accessing and manipulating box information.


# Spinny Task - Cuboid Box Inventory Management API

## API Testing with Postman

You can use [Postman](https://www.postman.com/) to test our API collection. Click the button below to import and run the collection in Postman:
- https://elements.getpostman.com/redirect?entityId=22717062-4ab68a79-2614-4829-a5fb-c534aa98b352&entityType=collection





## Author

[Ashutosh Sharma](www.linkedin.com/in/ashushm)









