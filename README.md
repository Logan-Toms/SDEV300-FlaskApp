# SDEV300-FlaskApp

## Overview
This repository contains a Flask web application developed as part of my college coursework. The project demonstrates my proficiency in Python and Flask, and my ability to create a web application that displays a list of recipes with their ingredients and steps, including user authentication and password management. This coursework is part of my Building Secure Python Applications (SDEV 300) class at the University of Maryland Global Campus.

## Table of Contents
1. [Project Purpose](#project-purpose)
2. [Key Skills Demonstrated](#key-skills-demonstrated)
3. [Project Impact](#project-impact)
4. [Files Included](#files-included)
5. [Usage Instructions](#usage-instructions)
6. [Technologies Used](#technologies-used)

## Project Purpose
The main objectives of this project are:
- To create a web application using Flask.
- To display a list of recipes with their ingredients and preparation steps.
- To implement user authentication (registration, login, and logout).
- To implement password validation and update functionalities.
- To handle routing, template rendering, and error handling in Flask.

## Key Skills Demonstrated
Throughout this project, I have gained and demonstrated skills in the following areas:
- **Web Development**: Building a web application using Flask.
- **Authentication**: Implementing user registration, login, and logout functionalities.
- **Password Management**: Validating and updating user passwords.
- **Routing and Templating**: Implementing routing and rendering HTML templates in Flask.
- **Error Handling**: Creating custom error pages for handling HTTP errors.
- **Python Programming**: Writing clean, modular, and reusable code in Python.

## Project Impact
This project has helped me:
- **Enhance Practical Skills**: Applied theoretical knowledge to practical scenarios, improving my understanding of web development with Flask.
- **Improve Problem-Solving Abilities**: Developed solutions for handling dynamic content, user authentication, password management, and error pages in a web application.
- **Develop User Interfaces**: Learned to design and implement effective web interfaces for displaying information and managing user sessions.

## Files Included
- `SDEV-Wk8-Lab8.py`: The main Python script that defines the Flask application and implements user authentication and password management.
- `templates/index.html`: The HTML template for the homepage displaying the list of recipes.
- `templates/recipe.html`: The HTML template for displaying the details of a specific recipe.
- `templates/register.html`: The HTML template for user registration.
- `templates/login.html`: The HTML template for user login.
- `templates/password_update.html`: The HTML template for updating user passwords.
- `templates/404.html`: The HTML template for the custom 404 error page.
- `static/images/`: Directory containing images used in the recipe pages.
- `CommonPassword.txt`: File containing a list of common passwords used for password validation.

## Usage Instructions
To run the application, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Logan-Toms/SDEV300-FlaskApp.git
    cd coursework-project
    ```

2. **Install Required Libraries**:
    Ensure you have Flask and Werkzeug installed. You can install them using pip:
    ```bash
    pip install flask werkzeug
    ```

3. **Set the FLASK_APP Environment Variable**:
    On Windows (PowerShell):
    ```powershell
    $env:FLASK_APP = "SDEV-Wk8-Lab8.py"
    ```

    On macOS and Linux:
    ```bash
    export FLASK_APP=SDEV-Wk8-Lab8.py
    ```

4. **Run the Application**:
    ```bash
    flask run
    ```

5. **Access the Application**:
    Open a web browser and go to `http://127.0.0.1:5000` to see the list of recipes. Register and log in to view detailed recipes and update your password.

## Technologies Used
- **Python**: The programming language used to develop the application.
- **Flask**: A micro web framework used for building the web application.
- **Werkzeug**: A comprehensive WSGI web application library used for password hashing and request handling.
- **HTML**: Used for creating the templates rendered by Flask.
- **Logging**: Used for recording failed login attempts.
