import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from cookbook import app, db

if os.path.exists("env.py"):
    import env  # noqa


# Database confuguration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# SQLite database file
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///cookbook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Create the database tables
with app.app_context():
    try:
        db.create_all()
        print("Database tables created successfully.")
    except Exception as e:
        print(f"Error creating database tables: {e}")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )  # Update to False before submitting
