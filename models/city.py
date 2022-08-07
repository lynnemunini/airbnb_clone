#!/usr/bin/env python3

"""
This module has a class City
that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines City attributes. Inherits
    from parent class BaseModel
    """

    state_id = ""  # it will be the State.id
    name = ""
