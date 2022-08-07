#!/usr/bin/env python3

"""
This module has a class Review
that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the Review attributes. Inherits
    from parent class BaseModel
    """

    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
