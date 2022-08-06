# AirBnB clone
![Holberton Image](assets/hbnb.png)

## Overview
The goal of this project is deploy a clone of [AirBnB website](https://www.airbnb.com/) on a server.

* The application is composed of a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and data (retrieve, create, delete, update them)

### The console
The console is a command interpreter that allows you to manipulate data without a visual interface. It let's us manage (create, update, destroy, etc) objects via a console / command interpreter and store and persist objects to a file (JSON file)

* `BaseModel` is a class that defines all common attributes/methods for other classes.
* The [base_model.py](models/base_model.py) contains the BaseModel class.
* [__init__.py](models/__init__.py) file lets Python interpreter know that a directory contains code for a Python module.
* `tests` directory contains tests for the project.

* `FileStorage` class serializes instances to a JSON file and deserializes JSON file to instances.
* [file_storage.py](models/engine/file_storage.py) contains the FileStorage class
* [console.py](console.py) contains the entry point to the interpreter.
* `User` class is a child class of BaseModel.
* [user.py](models/user.py) contains the User class.

The console validates this stoage engine.

![Console illustration](assets/console.png)

**TODO:** Include commands to start command interpreter

**TODO:** Describe how to start the command interpreter

**TODO:** Include examples of commands
