"""
Counter API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from service import status  # HTTP Status Codes
#from service import app

######################################################################
#  T E S T   C A S E S
######################################################################
class CounterTest(TestCase):
    """ REST API Server Tests """

    @classmethod
    def setUpClass(cls):
        """ This runs once before the entire test suite """
        #app.testing = True

    @classmethod
    def tearDownClass(cls):
        """ This runs once after the entire test suite """
        pass

    def setUp(self):
        """ This runs before each test """
        #self.app = app.test_client()

    def tearDown(self):
        """ This runs after each test """
        pass

######################################################################
#  T E S T   C A S E S 
######################################################################

    def test_something(self):
        """ Test something """
        self.assertTrue(True)
        # resp = self.app.get("/")
        # self.assertEqual(resp.status_code, status.HTTP_200_OK)
