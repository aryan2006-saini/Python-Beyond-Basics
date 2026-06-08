from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


@app.route('/')
def index():
    return {"message": "Drink API Running"}


# GET ALL DRINKS
@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()

    return {
        "drinks": [drink.to_dict() for drink in drinks]
    }


# GET DRINK BY ID
@app.route('/drinks/<int:id>', methods=['GET'])
def get_drink(id):
    drink = Drink.query.get_or_404(id)

    return drink.to_dict()


# ADD NEW DRINK
@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.get_json()

    drink = Drink(
        name=data['name'],
        description=data['description']
    )

    db.session.add(drink)
    db.session.commit()

    return {
        "message": "Drink added successfully",
        "drink": drink.to_dict()
    }, 201


# UPDATE DRINK
@app.route('/drinks/<int:id>', methods=['PUT'])
def update_drink(id):
    drink = Drink.query.get_or_404(id)

    data = request.get_json()

    drink.name = data['name']
    drink.description = data['description']

    db.session.commit()

    return {
        "message": "Drink updated successfully",
        "drink": drink.to_dict()
    }


# DELETE DRINK
@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)

    db.session.delete(drink)
    db.session.commit()

    return {
        "message": "Drink deleted successfully"
    }


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)