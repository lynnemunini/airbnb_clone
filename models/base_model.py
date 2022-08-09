#!/usr/bin/env python3

"""
This module contains a BaseModel class that defines all common
attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel is the parent class that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a aseModel instance
        """

        # re-create an instance with a dictionary representation
        if len(kwargs):
            # To make the BaseModel class inheritable
            # Don't hardcore assign values
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            # to have a unique id for each model
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".\
               format(str(self.__class__.__name__),
                      str(self.id), str(self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """

        # Work with dicctionary copy
        dictr = self.__dict__.copy()
        dictr["__class__"] = str(type(self).__name__)
        dictr["created_at"] = self.created_at.isoformat()
        dictr["updated_at"] = self.updated_at.isoformat()
        return dictr
