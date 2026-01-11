#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a new line for cleaner exit
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
