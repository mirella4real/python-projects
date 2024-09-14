import unittest

from coffee_machine import get_change

class TestGetChange(unittest.TestCase):
    def test_no_change(self):
        change = 0
        expected_change = 0
        self.assertEqual(get_change(change), expected_change)

    def test_less_than_dollar(self):
        change = 89
        expected_change = '0.89'
        self.assertEqual(get_change(change), expected_change)

    def test_more_than_dollar(self):
        change = 189
        expected_change = '1.89'
        self.assertEqual(get_change(change), expected_change)

if __name__ == "__main__":
    unittest.main()
