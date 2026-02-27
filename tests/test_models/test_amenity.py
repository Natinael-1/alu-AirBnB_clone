#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""
    def test_is_instance(self):
        """Test if instance is created correctly."""
        my_amenity = Amenity()
        self.assertTrue(isinstance(my_amenity, Amenity))
        self.assertTrue(hasattr(my_amenity, "id"))
        self.assertTrue(hasattr(my_amenity, "name"))
