#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        self._is_registered = False  # internal flag

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            # DO NOT register yet — tests expect this

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()

        # Register only once
        if not self._is_registered:
            storage.new(self)
            self._is_registered = True

        storage.save()

    def to_dict(self):
        new = self.__dict__.copy()
        new["__class__"] = self.__class__.__name__
        new["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new.pop("_is_registered", None)
        return new
