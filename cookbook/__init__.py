import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Create the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URL",
    'sqlite:///cookbook.db')

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Import the routes module to ensure the routes are registered
from cookbook import routes  # noqa
