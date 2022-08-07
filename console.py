#!/usr/bin/env python3
"""
Module that Contains the entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """
    intro = """
            Welcome to the AirBnB clone CLI.
            Type help to list commands, quit to exit.
            """

    # The prompt issued to solicit input.
    prompt = '(hbnb)'

    def emptyline(self):
        """
        Method called when an empty line is
        entered in response to the prompt
        """
        pass

    def do_quit(self, args):
        """
        Command quit to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Command EOF to exit the program
        """
        return True


# To make code not be executed when imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()
