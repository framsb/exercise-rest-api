"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import json
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Favorite_Character
import requests
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def handle_hello():
    user = User.query.all()
    all_user = list(map(lambda x: x.serialize(), user))
    response_body = {
        "message": all_user
    }
    return jsonify(response_body), 200


@app.route('/users/<int:id>', methods=['GET'])
def handle_user(id):
    user = User.query.get(id)
    if user is None:
        return "Not found",
    return jsonify(user.serialize()), 200
    

@app.route('/planets', methods=['GET'])
def handle_planets():
    planet = Planets.query.all()
    allplanets = list(map(lambda x: x.serialize(),planet))
    response_body = {
        "planets": allplanets
        }
    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def handle_characters():
    character = Characters.query.all()
    all_characters = list(map(lambda x: x.serialize(),character))
    response_body = {
        "characters": all_characters
        }
    return jsonify(response_body), 200

@app.route('/characters/<int:id>')
def handle_character(id):
    character = Characters.query.get(id)
    if character is None:
        return "Not Found", 404
    return jsonify(character.serialize())

@app.route('/planets/<int:id>')
def handle_planet(id):
    planet = Planets.query.get(id)
    if planet is None:
        return "Not Found", 404
    return jsonify(planet.serialize())

@app.route('/users/<int:userid>/favorite_character', methods=['GET'])
def handle_Favorites(userid):
    user_favorites = Favorite_Character.query.filter_by(userid= userid)
    all_favorites = list(map(lambda x: x.serialize(), user_favorites))
    return jsonify(all_favorites)
    
@app.route('/users/<int:userid>/favorite_character/<int:characterid>', methods=['POST','DELETE'])
def handle_favorite(userid,characterid):
    user = User.query.get(userid)
    if user is None:
        return "Not Found"
    if request.method == 'POST':
        FavCharacter = Favorite_Character(userid = userid , characterid = characterid)
        db.session.add(FavCharacter)
        db.session.commit()
        return jsonify(FavCharacter.serialize()), 201
    else:
        FavDelete = Favorite_Character.query.filter_by(userid = userid ,characterid=characterid).one_or_none()
        if FavDelete is None:
                return('not found in data base')
        else:
            db.session.delete(FavDelete)
            db.session.commit()
            return "Eliminated", 200
        
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
