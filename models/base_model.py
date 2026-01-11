#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""
import uuid
from datetime import datetime
from models import storage  # <--- LINK TO STORAGE


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance.
        """
        if kwargs:
            # Re-creating an existing instance (Do NOT add to storage)
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            # Creating a NEW instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # <--- ADD TO STORAGE

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute and saves to storage.
        """
        self.updated_at = datetime.now()
        storage.save()  # <--- SAVE TO FILE

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__. serialization
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

