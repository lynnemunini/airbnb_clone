#!/usr/bin/python3
"""Unittest for BaseModal class"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime, time, date
import os
import pep8


class TestBaseModel(unittest.TestCase):
    """Test cases for class BaseModel"""

    def setUp(self):
        """displace json file from it's position if it exits"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")

    def tearDown(self):
        """delete json file and return the original tests file"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_pep8(self):
        """Applying pep8 checker to my baseModel class"""
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "there's an error found in the model")

    def test_attribute(self):
        """test if a class has Id, created_at and updated_at"""
        sample = BaseModel()
        sample.name = "My_First_Model"
        sample.age = 22
        self.assertTrue(hasattr(sample, "name"))
        self.assertTrue(hasattr(sample, "age"))
        self.assertTrue(hasattr(sample, "id"))
        self.assertTrue(hasattr(sample, "created_at"))
        self.assertTrue(hasattr(sample, "updated_at"))


if __name__ == "__main__":
    unittest.main()
