# test_script.py
import unittest
from get_restaurant import get_restaurants

class TestGetRestaurants(unittest.TestCase):
    def test_get_restaurants(self):
        # Mock data for testing
        mock_api_key = "mock_api_key"
        
        # Call the function to get restaurants
        restaurants_data = get_restaurants(mock_api_key)

        # Assert that the returned data is not empty
        self.assertIsNotNone(restaurants_data)

        # Assert that the 'place_id' column exists in the DataFrame
        self.assertIn("place_id", restaurants_data.columns)

        # Add more assertions based on your specific conditions
        # For example, you can check if certain columns or values are present in the DataFrame

if __name__ == '__main__':
    unittest.main()
