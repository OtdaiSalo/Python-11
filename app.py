from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class AirFreshener(db.Model):
    id = db.Column(db.Integer,  nullable=False,  primary_key=True, autoincrement=True)
    price = db.Column(db.Float, nullable=False)
    costs_per_month = db.Column(db.Float, nullable=False)
    producer = db.Column(db.String, nullable=False)
    flavour = db.Column(db.String, nullable=False)
    volume = db.Column(db.Float, nullable=False)

    def __init__(self, price, costs_per_month, producer, flavour, volume):
        self.price = price
        self.costs_per_month = costs_per_month
        self.producer = producer
        self.flavour = flavour
        self.volume = volume


class FreshenerSchema(ma.Schema):
    class Meta:
        fields = ('price', 'costs_per_month', 'producer', 'flavour', 'volume')


air_freshener_schema = FreshenerSchema()
air_fresheners_schema = FreshenerSchema(many=True)
db.create_all()


@app.route("/air_freshener", methods=["POST"])
def add_air_freshener():
    price = request.json['price']
    costs_per_month = request.json['costs_per_month']
    producer = request.json['producer']
    flavour = request.json['flavour']
    volume = request.json['volume']

    new_air_freshener = AirFreshener(price, costs_per_month, producer, flavour, volume)

    db.session.add(new_air_freshener)
    db.session.commit()

    return air_freshener_schema.jsonify(new_air_freshener)


@app.route("/air_freshener", methods=["GET"])
def get_air_freshener():
    all_air_fresheners = AirFreshener.query.all()
    result = air_fresheners_schema.dump(all_air_fresheners)
    return jsonify(result.data)


@app.route("/air_freshener/<id>", methods=["GET"])
def air_freshener_detail(id):
    air_freshener = AirFreshener.query.get(id)
    return air_freshener_schema.jsonify(air_freshener)


@app.route("/air_freshener/<id>", methods=["PUT"])
def air_freshener_update(id):
    air_freshener = AirFreshener.query.get(id)

    price = request.json['price']
    costs_per_month = request.json['costs_per_month']
    producer = request.json['producer']
    flavour = request.json['flavour']
    volume = request.json['volume']

    air_freshener.price = price
    air_freshener.costs_per_month = costs_per_month
    air_freshener.producer = producer
    air_freshener.flavour = flavour
    air_freshener.volume = volume

    db.session.commit()
    return air_freshener_schema.jsonify(air_freshener)


@app.route("/air_freshener/<id>", methods=["DELETE"])
def air_freshener_delete(id):
    air_freshener = AirFreshener.query.get(id)
    db.session.delete(air_freshener)
    db.session.commit()

    return air_freshener_schema.jsonify(air_freshener)


if __name__ == '__main__':
    app.run()