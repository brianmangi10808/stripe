# data.py

from flask_sqlalchemy import SQLAlchemy
from model import db, User  # Import your SQLAlchemy instance and User model
from config import ApplicationConfig  # Import your application configuration

# Initialize SQLAlchemy with your Flask app configuration
def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(ApplicationConfig)
    db.init_app(app)
    return app

# Function to fetch all registered emails
def get_registered_emails():
    app = create_app()
    with app.app_context():
        # Query to fetch all emails
        users = User.query.all()
        email_list = [user.email for user in users]
        return email_list

if __name__ == "__main__":
    # Connect to the database and fetch emails
    registered_emails = get_registered_emails()
    print("Registered Emails:")
    for email in registered_emails:
        print(email)
