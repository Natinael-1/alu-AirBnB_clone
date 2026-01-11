#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file
    to instances.
    """
    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {}
        # Convert all objects in memory to dictionary representations
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        # Write the dictionary to the file in JSON format
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the file exists.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)

            for key, value in obj_dict.items():
                class_name = value["__class__"]
                if class_name in classes:
                    cls = classes[class_name]
                    self.new(cls(**value))
