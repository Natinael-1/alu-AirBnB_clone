#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    def test_is_instance(self):
        """Test if instance is created correctly."""
        my_user = User()
        self.assertTrue(isinstance(my_user, User))
        self.assertTrue(hasattr(my_user, "id"))
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
