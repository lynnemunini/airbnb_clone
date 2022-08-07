#!/usr/bin/env python3

"""
This module has a class Place
that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines Place attributes. Inherits
    from parent class BaseModel
    """

    city_id = ""  # it will be the City.id
    user_id = ""  # it will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # list of string it will be the list of Amenity.id
