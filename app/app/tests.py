"""
Sample tests
"""
from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """test adding numbers"""
        result = calc.add(5, 6)

        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """test subtracting number"""
        result = calc.subtract(10, 15)

        self.assertEqual(result, 5)