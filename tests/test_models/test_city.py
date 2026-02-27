#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class."""
    def test_is_instance(self):
        """Test if instance is created correctly."""
        my_city = City()
        self.assertTrue(isinstance(my_city, City))
        self.assertTrue(hasattr(my_city, "id"))
        self.assertTrue(hasattr(my_city, "state_id"))
