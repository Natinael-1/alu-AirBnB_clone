#!/usr/bin/python3
"""
This module contains the unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """Runs before every test."""
        self.my_model = BaseModel()

    def test_instance_creation(self):
        """Test if a BaseModel instance is created correctly"""
        self.assertTrue(isinstance(self.my_model, BaseModel))

    def test_id_is_string(self):
        """Test if the generated id is a string"""
        self.assertEqual(type(self.my_model.id), str)

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object"""
        self.assertEqual(type(self.my_model.created_at), datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object"""
        self.assertEqual(type(self.my_model.updated_at), datetime)

    def test_to_dict_returns_dictionary(self):
        """Test if to_dict() returns a valid dictionary"""
        model_dict = self.my_model.to_dict()
        self.assertEqual(type(model_dict), dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
