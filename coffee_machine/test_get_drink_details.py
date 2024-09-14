import unittest

from coffee_machine import get_drink_details

class TestGetDrinkDetails(unittest.TestCase):
    def test_bad_key(self):
        drink_order = 'asdfa'
        expected_result  = {
            'recipe': 'not found',
            'order': drink_order
        }
        self.assertEqual(get_drink_details(drink_order), expected_result)

    def test_get_cappuccino(self):
        drink_order = 'cappuccino'
        expected_result  = {
            'recipe': {
                'water':
                {
                    'unit': 'ml',
                    'amount': 250

                },
                'coffee':
                {
                    'unit': 'g',
                    'amount': 24
                },
                'milk':
                {
                    'unit': 'ml',
                    'amount': 100
                } 
            },
            'price': 300
        }
        self.assertEqual(get_drink_details(drink_order), expected_result)

    def test_get_latte(self):
        drink_order = 'latte'
        expected_result  = {
            'recipe': {
                'water':
                {
                    'unit': 'ml',
                    'amount': 200

                },
                'coffee':
                {
                    'unit': 'g',
                    'amount': 24
                },
                'milk':
                {
                    'unit': 'ml',
                    'amount': 150
                } 
            },
            'price': 250,
        }
        self.assertEqual(get_drink_details(drink_order), expected_result)

    def test_get_espresso(self):
        drink_order = 'espresso'
        expected_result  = { 
            'recipe': {
                'water':
                {
                    'unit': 'ml',
                    'amount': 50

                },
                'coffee':
                {
                    'unit': 'g',
                    'amount': 18
                }
            },
            'price': 150,
        }
        self.assertEqual(get_drink_details(drink_order), expected_result)

if __name__ == "__main__":
    unittest.main()