#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""
    def test_is_instance(self):
        """Test if instance is created correctly."""
        my_storage = FileStorage()
        self.assertTrue(isinstance(my_storage, FileStorage))
