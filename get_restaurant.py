import requests
import pandas as pd

<<<<<<< HEAD


=======
>>>>>>> origin/main
def get_restaurants(api_key):
    # Define search parameters for Munich
    munich_params = {
        "location": "48.1351,11.5820", # latitude,longitude of Munich
        "radius": 1000, # search radius in meters
        "type": "restaurant", # restrict search to restaurants
        "key": "AIzaSyBDpq5RceVsLNKiFAc9DuJLmIbinytbmTA" # API key
    }

    # Define search parameters for Berlin
    berlin_params = {
        "location": "52.5200,13.4050", # latitude,longitude of Berlin
        "radius": 1000, # search radius in meters
        "type": "restaurant", # restrict search to restaurants
        "key": "AIzaSyBDpq5RceVsLNKiFAc9DuJLmIbinytbmTA" # API key
    }

    # Define search parameters for Hamburg
    hamburg_params = {
        "location": "53.5511,9.9937", # latitude,longitude of Hamburg
        "radius": 1000, # search radius in meters
        "type": "restaurant", # restrict search to restaurants
        "key": "AIzaSyBDpq5RceVsLNKiFAc9DuJLmIbinytbmTA" # API key
    }

    # Send API requests and store data in DataFrame
    restaurants = pd.DataFrame(columns=["place_id", "name", "address", "rating"])
    for params in [munich_params, berlin_params, hamburg_params]:
        response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params)
        if response.status_code == 200:
            data = response.json()
            for restaurant in data["results"]:
                place_id = restaurant["place_id"]
                name = restaurant["name"]
                address = restaurant["vicinity"]
                rating = restaurant.get("rating", "-")
<<<<<<< HEAD
                restaurants = pd.concat([restaurants, pd.DataFrame({"place_id": place_id, "name": name, "address": address, "rating": rating}, index=[0])],ignore_index=True)

        else:
            print("Error: API request failed.")
    return restaurants
=======
                restaurants = restaurants.append({"place_id": place_id, "name": name, "address": address, "rating": rating}, ignore_index=True)
        else:
            print("Error: API request failed.")
    return restaurants

>>>>>>> origin/main
