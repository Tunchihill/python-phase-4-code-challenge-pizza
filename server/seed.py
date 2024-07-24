#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
  