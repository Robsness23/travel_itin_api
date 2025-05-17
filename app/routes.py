from flask import Blueprint, request, jsonify  # imports Blueprint (organises routes in modular way), request (access to incoming data - JSON from user), jsonify (turns python data to JSON)
from .models import db, User, Itinerary, Activity # brings in db connection and data models: User, Itinerary and Activity
from flask_jwt_extended import create_access_token, jwt_required # creates secure token when user logs in, secures routes so only logged in user can access them

api_bp = Blueprint ('api', __name__) #creating a group of routes (blueprint). Calling them 'api' and __name__ to tell Flask where the file is. 

@api_bp.route("/register", methods=["POST"]) # when someone sends a POST request to /register, this function runs 
def register() : # this defines the function that handles the register request 
    data = request.json # takes the incoming data from the user (username, password)
    user = User(username=data["username"], password=data["password"]) # creates a new User object, using the data just sent. Currently only storing the password in plain text, hashing will be done at later stage.
    db.session.add(user) # telling SQLAlchemy to add this new user to the db (not saved yet)
    db.session.commit() # saving the new user to the db
    return jsonify({"message": "User registered."}), 201 # sends back a success message in JSON format with HTTP status 201 (Created)

@api_bp.route("/login", methods=["POST"]) # when someone send a POST request to /login, this function runs 
def login () : # defining the login function 
    data = request.json # gets the username and password from the incoming request 
    user = User.query.filter_by(username=data["username"]).first() # checks db for first user with that username
    if user and user.password == data["password"] : # this checks if the user exists & if the password matches  - still need to add hashing
        token = create_access_token(identity=user.id) # if password is valid, generate a JWT token that identifies the user by their id. 
        return jsonify (["token" : token]) # sends the token back to the user - which they will use for future requests
    return jsonify({"message": "Invalid credentials"}), 401 # if login fails, return message with HTTP status code 401 (Unauthorized)

@api_bp.route("/itineraries", method=["GET"]) # defines a GET route at /itineraries 
@jwt_required() # only logged in user (with valid token) can access this 
def get_itineraries () : # starts the function to handle the request 
    itineraries = Itinerary.query.all() # gets all itineraries from the db
    return jsonify([{"title": i.title, "destination": i.destination} for i in itineraries]) # sends back a list of all JSON itineraries, only showing the title and destination for each one. 



    

