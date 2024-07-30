""" This is a Flask app that displays a list of recipes and their ingredients and steps. """

from datetime import datetime
from functools import wraps
import logging
import re
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 


recipes = [  # Dictionary of recipes
    {
        'id': 1,
        'title': 'Python Programming Pasta',
        'ingredients': [
            'Spaghetti', 'Black olives', 'Green bell peppers', 'Red cherry tomatoes',
            'Garlic cloves', 'Olive oil', 'Salt and Pepper (to taste)',
            'Grated Parmesan cheese (optional)', 'Fresh basil (for garnish)'
        ],
        'steps': [
            """Boil water in a large pot, add a pinch of salt, and cook the spaghetti until al 
            dente. Drain and set aside.""",
            """Heat olive oil in a pan over medium heat. Add finely chopped garlic and cook until 
            fragrant.""",
            'Slice the black olives and green bell peppers into small pieces.',
            'Add them to the pan and sauté for a few minutes.',
            'Add the cooked spaghetti to the pan with the vegetables.',
            'Toss everything together to combine.',
            'Slice the cherry tomatoes in half and add them to the pasta.',
            'Season with salt and pepper to taste.',
            """Serve the pasta in a dish, garnish with fresh basil leaves, and if desired, 
            sprinkle with grated Parmesan cheese.""",
            """ For presentation, arrange the pasta to resemble Python code structure, such as 
            loops or functions, on the plate."""
        ],
        'TotalTime': '30 minutes',
        'Difficulty': 'Easy',
        'image': '/static/images/Python-Programming-Pasta.png'
    },
    {
        'id': 2,
        'title': 'JavaScript Jambalaya',
        'ingredients': [
            'Chicken breast', 'Andouille sausage', 'Shrimp', 'Long-grain rice',
            'Onion', 'Green bell pepper', 'Celery', 'Garlic cloves', 'Canned tomatoes',
            'Chicken broth', 'Cajun seasoning', 'Bay leaves', 'Thyme', 'Salt and pepper'
        ],
        'steps': [
            'Cut chicken and sausage into bite-sized pieces and season with Cajun seasoning.',
            'In a large pot, sauté onion, bell pepper, and celery in olive oil until softened.',
            'Add garlic, chicken, and sausage to the pot and cook until the chicken is browned.',
            'Stir in rice, canned tomatoes, chicken broth, bay leaves, and thyme.',
            'Bring to a boil, then reduce heat to simmer and cover for 20 minutes.',
            'Add shrimp to the pot and cook for another 5 minutes or until the shrimp is pink.',
            'Season with salt and pepper to taste and serve with a garnish of green onions.'
        ],
        'TotalTime': '1 hour',
        'Difficulty': 'Medium',
        'image': '/static/images/JavaScript-Jambalaya.png'
    },
    {
        'id': 3,
        'title': 'HTML Hummus Platter',
        'ingredients': [
            'Chickpeas', 'Tahini', 'Lemon juice', 'Garlic cloves',
            'Olive oil', 'Paprika', 'Cumin', 'Salt', 'Fresh parsley',
            'Vegetables for dipping (carrots, cucumbers, bell peppers)'
        ],
        'steps': [
            'In a food processor, blend chickpeas, tahini, lemon juice, and garlic until smooth.',
            'While blending, slowly add olive oil until you reach the desired consistency.',
            'Season the hummus with paprika, cumin, and salt to taste.',
            'Transfer to a serving dish and garnish with fresh parsley.',
            'Serve with a selection of fresh vegetables for dipping.'
        ],
        'TotalTime': '15 minutes',
        'Difficulty': 'Easy',
        'image': '/static/images/HTML-Hummus-Platter.png'
    },
    {
        'id': 4,
        'title': 'CSS Caesar Salad',
        'ingredients': [
            'Romaine lettuce', 'Croutons', 'Parmesan cheese', 'Caesar dressing',
            'Lemon wedges', 'Anchovy fillets (optional)', 'Garlic cloves',
            'Olive oil', 'Dijon mustard', 'Worcestershire sauce'
        ],
        'steps': [
            'Wash and chop the romaine lettuce and place it in a large salad bowl.',
            '''Prepare the dressing by mixing olive oil, crushed garlic, Dijon mustard, and 
            Worcestershire sauce.''',
            'Toss the lettuce with croutons, grated Parmesan cheese, and the dressing.',
            'Serve with lemon wedges and anchovy fillets on top, if desired.'
        ],
        'TotalTime': '20 minutes',
        'Difficulty': 'Easy',
        'image': '/static/images/CSS-Caesar-Salad.png'
    },
]

# User database simulation
users = {}


# Route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register user if username is not already taken."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if username in users:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))

        # Validate password
        is_valid, message = validate_password(password)
        if not is_valid:
            flash(message)
            return redirect(url_for('register'))

        # Register new user
        users[username] = generate_password_hash(password)
        return redirect(url_for('login'))

    return render_template('register.html')


# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log in user if username and password match."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        client_ip = request.remote_addr  # Get client IP address

        # Check if username exists
        if username not in users:
            log_failed_login(client_ip)
            flash('Invalid username')
            return render_template('login.html')

        # Check if password is correct
        if not check_password_hash(users[username], password):
            log_failed_login(client_ip)
            flash('Incorrect password')
            return render_template('login.html')

        # If both checks pass, log in the user
        session['username'] = username
        return redirect(url_for('password_update'))  # Redirect to password update page

    return render_template('login.html')


# Route for password update
@app.route('/password_update', methods=['GET', 'POST'])
def password_update():
    """Update user password."""
    if request.method == 'POST':
        # Retrieve username from the session
        username = session.get('username')
        if not username or username not in users:
            # If no user is logged in, or found in users dict, redirect to the login page
            return redirect(url_for('login'))

        # Fetch the user's password hash
        user_password_hash = users[username]

        # Get form data
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Check if the old password is correct
        if not check_password_hash(user_password_hash, old_password):
            flash('Old password is incorrect.')
            return redirect(url_for('password_update'))

        # Check if new password matches the confirmation
        if new_password != confirm_password:
            flash('New password and confirmation do not match.')
            return redirect(url_for('password_update'))

        # Validate new password
        is_valid, message = validate_password(new_password)
        if not is_valid:
            flash(message)
            return redirect(url_for('password_update'))

        # Update the user's password in the dictionary
        users[username] = generate_password_hash(new_password)

        return redirect(url_for('index'))  # Redirect to the home page

    # Display the password update form
    return render_template('password_update.html')


# Route for logout
@app.route('/logout')
def logout():
    """Log out user."""
    # Remove the username from the session
    session.pop('username', None)
    # Redirect to login page or another appropriate page
    return redirect(url_for('login'))


# Apply login required decorator
def login_required(f):
    """Function to require login for certain routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# Modify existing routes to include login_required decorator
@app.route('/')
def index():
    """Return the homepage with a list of recipes."""
    return render_template('index.html', recipes=recipes, current_time=datetime.now())


# Recipe route
@app.route('/recipe/<int:recipe_id>')
@login_required  # Now requires login
def recipe(recipe_id):
    """Return the recipe page with the recipe that matches the given ID."""
    selected_recipe = next(
        (item for item in recipes if item["id"] == recipe_id), None)
    if selected_recipe is None:
        return render_template('404.html'), 404
    return render_template('recipe.html', recipe=selected_recipe, current_time=datetime.now())


# Error handler, 404
@app.errorhandler(404)
def page_not_found():
    """Return a custom 404 error page."""
    return render_template('404.html'), 404


def validate_password(password):
    """Validate the password against specific criteria and common passwords list."""

    # Check if the password meets the basic criteria
    if len(password) < 12:
        return False, "Password must be at least 12 characters long."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."

    # Check against the list of common passwords
    with open('CommonPassword.txt', 'r', encoding='utf-8') as file:
        common_passwords = file.read().splitlines()
        if password in common_passwords:
            return False, "Password is too common. Please select a different secret."

    return True, "Password is valid."


# Setup basic configuration for logging
logging.basicConfig(filename='failed_login_attempts.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


# function to log failed login attempts
def log_failed_login(ip_address):
    """Log failed login attempts with date, time, and IP address."""
    logging.info("Failed login attempt from %s", ip_address)

if __name__ == '__main__':
    app.run(debug=True)
