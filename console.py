#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter.
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class.
    """
    prompt = '(hbnb) '
    
    # A dictionary to map string names to actual classes
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Create the instance
        new_instance = HBNBCommand.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        
        if not args:
            print("** class name missing **")
            return
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        
        if not args:
            print("** class name missing **")
            return
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objs = storage.all()
        obj_list = []

        # If no class name provided, print ALL objects
        if not args:
            for obj in all_objs.values():
                obj_list.append(str(obj))
            print(obj_list)
            return

        # If class name provided, print only those objects
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        for key, obj in all_objs.items():
            # Check if the object belongs to the requested class
            if key.startswith(args[0]):
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg) # shlex helps handle quotes: name "Betty"
        
        if not args:
            print("** class name missing **")
            return
        
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        
        if key not in all_objs:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = args[2]
        attr_val = args[3]

        # Casting logic: Convert string "30" to int 30, "5.5" to float 5.5
        try:
            if "." in attr_val:
                attr_val = float(attr_val)
            else:
                attr_val = int(attr_val)
        except ValueError:
            pass # Keep it as a string

        setattr(obj, attr_name, attr_val)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
