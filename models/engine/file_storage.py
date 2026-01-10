#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""
import json
import os

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
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
        from models.base_model import BaseModel  # Import here to avoid circular dependency
        
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                
            # Loop through the dictionary and recreate the objects
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                if class_name == "BaseModel":
                    # Create a new instance of BaseModel using the dictionary
                    obj = BaseModel(**value)
                    # Add it to the storage
                    self.new(obj)
