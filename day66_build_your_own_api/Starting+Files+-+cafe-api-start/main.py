from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import copy

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

error_msg = {"error": {
    "Not Found": "Sorry, we don't have a cafe at that location"
}}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    all_cafes = db.session.query(Cafe).all()
    cafe = random.choice(all_cafes)
    return jsonify(cafe=cafe.to_dict())
    # return jsonify(id=cafe.id, name=cafe.name, map_url=cafe.map_url, img_url=cafe.img_url, location=cafe.location, seats=cafe.
    #         seats, has_toilet=cafe.has_toilet, has_wifi=cafe.has_wifi, has_sockets=cafe.has_sockets, can_take_calls=cafe.
    #         can_take_calls, coffee_price=cafe.coffee_price)


@app.route("/all")
def all_cafes():
    all_cafes = db.session.query(Cafe).all()
    cafe_dict = {cafe.id: cafe.to_dict() for cafe in all_cafes}
    return jsonify(cafe_dict)


@app.route("/search")
def search_cafe():
    location = request.args.get("loc").title()
    target_cafe = db.session.query(Cafe).filter_by(location=location).first()
    if target_cafe:
        return jsonify(target_cafe.to_dict())
    else:
        return jsonify(error_msg)


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(name=request.args.get("name"),
                    map_url=request.args.get("map_url"),
                    img_url=request.args.get("img_url"),
                    location=request.args.get("location"),
                    seats=request.args.get("seats"),
                    has_toilet=bool(request.args.get("has_toilet")),
                    has_wifi=bool(request.args.get("has_wifi")),
                    has_sockets=bool(request.args.get("has_sockets")),
                    can_take_calls=bool(request.args.get("can_take_calls")),
                    coffee_price=request.args.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"response": {"success": "Successfully added the new cafe."}})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def change_price(cafe_id):
    target_cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    print(target_cafe)
    if target_cafe is None:
        return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found"}})
    else:
        new_price = request.args.get("new_price")
        target_cafe.price = new_price
        return jsonify({"Sucess": "Sucessfully updated the price."})


@app.route("/delete", methods=["DELETE"])
def delete_cafe():
    api_key = request.args.get("api-key")
    cafe_id = request.args.get("cafe_id")
    if api_key == "dsfswjkl;jtklnb":
        target_cafe = db.session.query(Cafe).get(cafe_id)
        if target_cafe is None:
            return jsonify({"error": "Sorry, there's no cafe with the corresponding cafe_id"})
        else:
            cafe_name = copy.deepcopy(target_cafe.name)
            db.session.delete(target_cafe)
            db.session.commit()
            return jsonify({"Success": f"Successfully deleted {cafe_name}"})
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key"})


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
