import unittest
from flask import Flask
from app import app, BMRForm, calculate_bmr

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_calculate_bmr(self):
        # Create a test form data
        form_data = {
            'gender': 'male',
            'height_ft': 5,
            'height_in': 10,
            'weight': 150,
            'age': 30,
            'activity_level': 'sedentary'
        }

        # Send POST request to the 'calculate' route with the test form data
        response = self.app.post('/', data=form_data)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the BMR result is in the response
        bmr = calculate_bmr(**form_data)
        self.assertIn(str(bmr), response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()