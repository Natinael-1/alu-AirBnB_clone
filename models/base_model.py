#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new BaseModel instance.
        """
        # Assign a random UUID (converted to string)
        self.id = str(uuid.uuid4())
        
        # Assign the current date and time
        self.created_at = datetime.now()
        
        # Assign the update time (initially same as creation)
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        # 1. Create a COPY of the dictionary so we don't mess up the original object
        new_dict = self.__dict__.copy()
        
        # 2. Add the class name to the dictionary
        new_dict["__class__"] = self.__class__.__name__
        
        # 3. Convert the datetime objects to ISO format strings
        # We use isoformat() because JSON cannot understand Python 'datetime' objects,
        # but it understands Strings perfectly.
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        
        return new_dict
