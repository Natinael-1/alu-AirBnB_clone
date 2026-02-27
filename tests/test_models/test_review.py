#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class."""
    def test_is_instance(self):
        """Test if instance is created correctly."""
        my_review = Review()
        self.assertTrue(isinstance(my_review, Review))
        self.assertTrue(hasattr(my_review, "id"))
        self.assertTrue(hasattr(my_review, "place_id"))
