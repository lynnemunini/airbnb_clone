#!/usr/bin/env python3
"""
This module contains a file storage class that converts
the dictionary representation to a json string(serialization)
and a json string to an object(deserialization)
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that converts a dictionary representation to a json string
    and vice versa
    """
    # private class attributes
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """
        Returns private class attributes __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dictr = {key: value.to_dict() for key, value in self.__objects.items()}

        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictr, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)
        """
        if os.path.isfile(self.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                dictr = json.load(f)
                for key, value in dictr.items():
                    FileStorage.__objects[key] = eval(
                            key.split(".")[0])(**value)
