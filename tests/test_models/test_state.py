#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class."""
    def test_is_instance(self):
        """Test if instance is created correctly."""
        my_state = State()
        self.assertTrue(isinstance(my_state, State))
        self.assertTrue(hasattr(my_state, "id"))
        self.assertTrue(hasattr(my_state, "name"))
