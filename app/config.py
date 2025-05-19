import os

class Config: # storing all the apps settings in this class
    SECRET_KEY = "supersecretkey" # adding in Flask's security setting 
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/travel_db") # telling Flask how to connect to the db, if it cannot use db url, then it can resort to using the the other url. I will update user, password, and travel_db to match your actual database settings once actioned.
    SQLALCHEMY_TRACK_MODIFICATIONS = False # disabling feature that tracks changes to make things quicker
    JWT_SECRET_KEY = "jwt-secret-string" # used to sign and verify JWT tokens. To be kept secret in prod.

    # this is for everything config related. Security keys, db connection and JWT token setup.

