#!/usr/bin/env python3
"""
Module that Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """

    # The prompt issued to solicit input.
    prompt = '(hbnb)'

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
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            models.storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        objects = models.storage.all()
        classes = ['BaseModel']

        if len(arg) == 0:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in classes:
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
        objects = models.storage.all()
        args = arg.split(' ')

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1 and args[0] == "BaseModel":
            print("** instance id missing **")
        else:
            del objects[f"{args[0]}.{args[1]}"]
            models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = arg.split(' ')
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_list = []
            for obj in models.storage.all().values():
                my_list.append(str(obj))
            print(my_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        objects = models.storage.all()
        args = arg.split(' ')

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1 and args[0] == "BaseModel":
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
        else:
            for key, value in objects.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1]:
                    if len(arg) == 2:
                        print(" ** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, args[2], args[3])
                        models.storage.save()


# To make code not be executed when imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()
