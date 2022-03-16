from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

# TODO 0 : setup Flask and DB
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TODO 1: Cafe Model
##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

    # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# TODO 2 : Create RESTful Router

@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random")
def random_cafe():
    all_cafes = db.session.query(Cafe).all()
    print(type(all_cafes))
    cafe = random.choice(all_cafes)
    return jsonify(cafe=cafe.to_dict())
    # return jsonify(id=cafe.id, name=cafe.name, map_url=cafe.map_url, img_url=cafe.img_url, location=cafe.location, seats=cafe.
    #         seats, has_toilet=cafe.has_toilet, has_wifi=cafe.has_wifi, has_sockets=cafe.has_sockets, can_take_calls=cafe.
    #         can_take_calls, coffee_price=cafe.coffee_price)


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
