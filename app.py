from flask import Flask,request
from flask_restful import Resource , Api, reqparse
from flask_jwt import JWT ,jwt_required
from security import authenticate,identity

from resources.users import UserRegister
from resources.item import Item,ItemsList
from resources.store import StoreList,Store


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "keshav"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)   # /auth


api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, "/register")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
    