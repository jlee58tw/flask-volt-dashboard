# -*- encoding: utf-8 -*-

from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from apps import db

from apps.authentication.util import hash_pass

# series episodes

class Dessert(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # A dessert has a name, a price and some calories:
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    calories = db.Column(db.Integer)

    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def calories_per_dollar(self):
        if self.calories:
            return self.calories / self.price

# class Users(db.Model, UserMixin):

#     __tablename__ = 'Users'

#     id            = db.Column(db.Integer, primary_key=True)
#     username      = db.Column(db.String(64), unique=True)
#     email         = db.Column(db.String(64), unique=True)
#     password      = db.Column(db.LargeBinary)

#     oauth_github  = db.Column(db.String(100), nullable=True)

#     def __init__(self, **kwargs):
#         for property, value in kwargs.items():
#             # depending on whether value is an iterable or not, we must
#             # unpack it's value (when **kwargs is request.form, some values
#             # will be a 1-element list)
#             if hasattr(value, '__iter__') and not isinstance(value, str):
#                 # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
#                 value = value[0]

#             if property == 'password':
#                 value = hash_pass(value)  # we need bytes here (not plain str)

#             setattr(self, property, value)

#     def __repr__(self):
#         return str(self.username) 
