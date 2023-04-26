import pandas as pd
from get_restaurant import get_restaurants
from restaurant_data_to_mysql import load_to_mysql

# Get restaurants data
restaurants = get_restaurants(api_key="AIzaSyBDpq5RceVsLNKiFAc9DuJLmIbinytbmTA")


load_to_mysql(df=restaurants, host="127.0.0.1", user="root", password="root", database="api_de_project",port=3307, table="restaurants")




