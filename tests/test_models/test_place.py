#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""
    def test_is_instance(self):
        """Test if instance is created correctly."""
        my_place = Place()
        self.assertTrue(isinstance(my_place, Place))
        self.assertTrue(hasattr(my_place, "id"))
        self.assertTrue(hasattr(my_place, "city_id"))
