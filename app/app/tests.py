"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc

class testcalc(SimpleTestCase):
    def test_multiply_numbers(self):
        """test for adding numbers"""
        result = calc.add(4,5)
        self.assertEqual(result, 9)

    def test_substract_numbers(self):
        """test for substracting numbers"""    
        result = calc.substract(15,10)
        self.assertEqual(result, 5)

        