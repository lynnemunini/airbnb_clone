#1/usr/bin/env python3
"""
Defines unittests for the class User
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
   Tests for the User class
    """
    def test_instantiation(self):
        userA = User()
        userB = User()
        self.assertNotEqual(userA.id, userB.id)
