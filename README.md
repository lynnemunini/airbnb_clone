# AirBnB clone

![Holberton Image](assets/hbnb.png)

## Overview

The goal of this project is deploy a clone of [AirBnB website](https://www.airbnb.com/) on a server.

* The application is composed of a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and data (retrieve, create, delete, update them)

<br>
<br>

### The console

The console is a command interpreter that allows you to manipulate data without a visual interface. It let's us manage (create, update, destroy, etc) objects via a console / command interpreter and store and persist objects to a file (JSON file)

* `BaseModel` is a class that defines all common attributes/methods for other classes.
* The [base_model.py](models/base_model.py) contains the BaseModel class.
* [__init__.py](models/__init__.py) file lets Python interpreter know that a directory contains code for a Python module.
* `tests` directory contains unittests for the classes defined in the `models` directory.

* `FileStorage` class serializes instances to a JSON file and deserializes JSON file to instances.
* [file_storage.py](models/engine/file_storage.py) contains the FileStorage class
* [console.py](console.py) contains the entry point to the interpreter.
* `User` class is a child class of BaseModel.
* [user.py](models/user.py) contains the User class.
* More information about the classes can be found in the [models](models/) directory.

**The console validates this stoage engine.*

![Console illustration](assets/console.png)

**Command Interpreter**

To start the interpreter, type `./console.py` in the terminal. To quit the interpreter, type `quit` for help on the console commands, type `help` to see all the available commands, type `help <command>` to see the help for a specific command.

You can use the commands `create` Ex: `create BaseModel`, 
`show` Ex: `show BaseModel 1234-1234-1234`, 
`destroy` Ex: `destroy BaseModel 1234-1234-1234`, 
`all` Ex: `all BaseModel` and 
`update` Ex: `update BaseModel 1234-1234-1234 email "aibnb@mail.com"` to manipulate objects. `update <class name> <id> <attribute name> "<attribute value>"`

*Example:*
To create a new user, type `create User`.
To show all users, type `all User`.
To delete a user, type `destroy User <id>`. You can find the id of the user in the `all` command.

See below code snippets for more information.

```
(hbnb) create User
52eca31c-a644-4363-a868-ec9cff30b32e
(hbnb) show User 52eca31c-a644-4363-a868-ec9cff30b32e
[User] (52eca31c-a644-4363-a868-ec9cff30b32e) {'id': '52eca31c-a644-4363-a868-ec9cff30b32e', 'created_at': datetime.datetime(2022, 8, 9, 14, 18, 19, 112740), 'updated_at': datetime.datetime(2022, 8, 9, 14, 18, 19, 112757)}
(hbnb) all User
["[User] (52eca31c-a644-4363-a868-ec9cff30b32e) {'id': '52eca31c-a644-4363-a868-ec9cff30b32e', 'created_at': datetime.datetime(2022, 8, 9, 14, 18, 19, 112740), 'updated_at': datetime.datetime(2022, 8, 9, 14, 18, 19, 112757)}"]
(hbnb) create User
76cbeb7a-c450-4bf3-823c-a565074acc4f
(hbnb) destroy User 76cbeb7a-c450-4bf3-823c-a565074acc4f
(hbnb) create User
897fdef6-a49e-45ea-b5c2-686f676e16c0
(hbnb) all User
["[User] (52eca31c-a644-4363-a868-ec9cff30b32e) {'id': '52eca31c-a644-4363-a868-ec9cff30b32e', 'created_at': datetime.datetime(2022, 8, 9, 14, 18, 19, 112740), 'updated_at': datetime.datetime(2022, 8, 9, 14, 18, 19, 112757)}", "[User] (897fdef6-a49e-45ea-b5c2-686f676e16c0) {'id': '897fdef6-a49e-45ea-b5c2-686f676e16c0', 'created_at': datetime.datetime(2022, 8, 9, 14, 28, 26, 678376), 'updated_at': datetime.datetime(2022, 8, 9, 14, 28, 26, 678398)}"]
(hbnb) create Place
35aa319d-728f-4a04-8802-ad202a06cb59
(hbnb) show User 897fdef6-a49e-45ea-b5c2-686f676e16c0
[User] (897fdef6-a49e-45ea-b5c2-686f676e16c0) {'id': '897fdef6-a49e-45ea-b5c2-686f676e16c0', 'created_at': datetime.datetime(2022, 8, 9, 14, 28, 26, 678376), 'updated_at': datetime.datetime(2022, 8, 9, 14, 28, 26, 678398)}
(hbnb) update User 897fdef6-a49e-45ea-b5c2-686f676e16c0 email "munini@gmail.com"
(hbnb) show User 897fdef6-a49e-45ea-b5c2-686f676e16c0
[User] (897fdef6-a49e-45ea-b5c2-686f676e16c0) {'id': '897fdef6-a49e-45ea-b5c2-686f676e16c0', 'created_at': datetime.datetime(2022, 8, 9, 14, 28, 26, 678376), 'updated_at': datetime.datetime(2022, 8, 9, 14, 28, 26, 678398), 'email': 'munini@gmail.com'}
(hbnb) 
```

```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
daec2e8c-43bb-4af7-b7f8-c94ba930ed41
(hbnb) all BaseModel
["[BaseModel] (daec2e8c-43bb-4af7-b7f8-c94ba930ed41) {'id': 'daec2e8c-43bb-4af7-b7f8-c94ba930ed41', 'created_at': datetime.datetime(2022, 8, 9, 14, 34, 25, 147642), 'updated_at': datetime.datetime(2022, 8, 9, 14, 34, 25, 147658)}"]
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel daec2e8c-43bb-4af7-b7f8-c94ba930ed41 first_name "Mark"
(hbnb) show BaseModel daec2e8c-43bb-4af7-b7f8-c94ba930ed41
[BaseModel] (daec2e8c-43bb-4af7-b7f8-c94ba930ed41) {'id': 'daec2e8c-43bb-4af7-b7f8-c94ba930ed41', 'created_at': datetime.datetime(2022, 8, 9, 14, 34, 25, 147642), 'updated_at': datetime.datetime(2022, 8, 9, 14, 34, 25, 147658), 'first_name': 'Mark'}
(hbnb) create BaseModel
795dd79f-8042-40c9-82c0-17f2ae936112
(hbnb) all BaseModel
["[BaseModel] (daec2e8c-43bb-4af7-b7f8-c94ba930ed41) {'id': 'daec2e8c-43bb-4af7-b7f8-c94ba930ed41', 'created_at': datetime.datetime(2022, 8, 9, 14, 34, 25, 147642), 'updated_at': datetime.datetime(2022, 8, 9, 14, 34, 25, 147658), 'first_name': 'Mark'}", "[BaseModel] (795dd79f-8042-40c9-82c0-17f2ae936112) {'id': '795dd79f-8042-40c9-82c0-17f2ae936112', 'created_at': datetime.datetime(2022, 8, 9, 14, 35, 55, 347099), 'updated_at': datetime.datetime(2022, 8, 9, 14, 35, 55, 347118)}"]
(hbnb) destroy BaseModel 795dd79f-8042-40c9-82c0-17f2ae936112
(hbnb) show BaseModel 795dd79f-8042-40c9-82c0-17f2ae936112
** no instance found **
(hbnb) 
```

A unique id is assigned to each object on creation.

<br>
<br>

### Web static

This section describes the Front-end of the application. Each page is rendered by a template.

**This image illustrates how the application is rendered.**

![FrontEnd Illumination](assets/web-static.png)

The front end is implemented using HTML markup and CSS.
