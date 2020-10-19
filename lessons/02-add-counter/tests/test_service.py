"""
Counter API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from flask_api import status  # HTTP Status Codes
from service.routes import app, reset_counter

######################################################################
#  T E S T   C A S E S
######################################################################
class CounterTest(TestCase):
    """ REST API Server Tests """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        app.testing = True

    @classmethod
    def tearDownClass(cls):
        """ This runs once after the entire test suite """
        pass

    def setUp(self):
        """ This runs before each test """
        reset_counter()
        self.app = app.test_client()


    def tearDown(self):
        """ This runs after each test """
        pass

######################################################################
#  T E S T   C A S E S 
######################################################################

    def test_index(self):
        """ Test index call """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_counter(self):
        """ Test Get counter """
        resp = self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(data["counter"], 1)

    def test_get_increments_counter(self):
        """ Test Get increments the counter """
        resp = self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(data["counter"], 1)
        # increment 3 times
        self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.app.get("/counter")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.get_json()
        self.assertEqual(data["counter"], 4)
