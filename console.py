#!/usr/bin/env python3
"""
Module that Contains the entry point of the command interpreter
"""
import cmd


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


# To make code not be executed when imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()
