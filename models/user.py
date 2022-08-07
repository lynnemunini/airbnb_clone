#!/usr/bin/env python3

"""
This module has a class User that inherits
from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    # Public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # TODO: Update console.py to allow show, create
    # destroy, update and all used with User
