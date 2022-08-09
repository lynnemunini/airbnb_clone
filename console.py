#!/usr/bin/env python3
"""
Module that Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """

    # The prompt issued to solicit input.
    prompt = '(hbnb) '
    __class = ["BaseModel", "User", "Amenity", "City",
               "Place", "Review", "State"]

    def emptyline(self):
        """
        Method called when an empty line is
        entered in response to the prompt
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Command EOF to exit the program
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        args = arg.split(' ')
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        objects = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] == "BaseModel":
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            print(objects[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        objects = storage.all()
        args = arg.split(' ')

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
        elif len(arg) == 1 and args[0] in HBNBCommand.__class:
            print("** instance id missing **")
        else:
            del objects[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        if not arg:
            dictr = []
            for key, value in storage.all().items():
                dictr.append(str(value))
            if dictr != 0:
                print(dictr)
        else:
            arg = arg.split()
            if arg[0] in HBNBCommand.__class:
                dictr = []
                for key, value in storage.all().items():
                    if str(key.split(".")[0]) == arg[0]:
                        dictr.append(str(value))
                if dictr != 0:
                    print(dictr)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return
        new_arg = shlex.split(arg)
        if new_arg[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
            return
        elif len(new_arg) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                j = new_arg[0] + "." + new_arg[1]
                storage.all()[j]
            except Exception:
                print("** no instance found **")
                return
        if len(new_arg) == 2:
            print("** attribute name missing **")
        elif len(new_arg) == 3:
            print("** value missing **")
        else:
            j = new_arg[0] + "." + new_arg[1]
            if new_arg[3] is float:
                value = float(new_arg[3])  # casting value unto it datatype
            elif new_arg[3] is int:
                value = int(new_arg[3])
            else:
                value = str(new_arg[3].strip(":\"'"))
            setattr(storage.all()[j], new_arg[2].strip(":\"'"), value)
            storage.save()


# To make code not be executed when imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()
