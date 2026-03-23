# Gym Log Application
This is a simple web application to log gym exercise sessions and search through them. Built with Python, Flask and SQLite.
## Features
- User registration and login with hashed passwords
- Add new exercises with descriptions and categories
- Search exercises by name or description
- Categories right now are Upper Body, Legs and Cardio
## Prerequisites
- Python 3.11.9
- Virtual environment venv
## Installation & Setup
- Clone the repository
- Create and activate a virtual environment ("python -m venv venv"; "venv\Scripts\activate")
- Install the dependencies ("pip install -r requirements.txt")
- Initialize the database ("python setup_db.py")
- And then run the app ("python app.py")
- The app should now be available at http://127.0.0.1:5000
