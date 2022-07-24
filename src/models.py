from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    favorite_character = db.relationship('Favorite_Character', lazy=True)
    favorite_planet = db.relationship('Favorite_Planet', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    gravity = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(60), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(60), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gravity":self.gravity,
            "terrain": self.terrain,
            "population": self.population,
            "climate": self.climate,
        }
        
class Characters(db.Model):
    __tablename__= "characters"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(60),nullable=False)
    eyes = db.Column(db.String(60), nullable=False)
    hair = db.Column(db.String(60),nullable=False)
    birth_year = db.Column(db.String(60), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname":self.lastname,
            "gender": self.gender,
            "eyes": self.eyes,
            "hair": self.hair,
            "birth_year": self.birth_year,
        }
        
class Favorite_Character(db.Model):
    __tablename__="favorite_character"
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    characterid = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def serialize(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "characterid": self.characterid,
        }
class Favorite_Planet(db.Model):
    __tablename__="favorite_planet"
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    planetsid = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def serialize(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "planetsid": self.planetsid,
        }