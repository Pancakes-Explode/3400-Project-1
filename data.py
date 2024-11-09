from ast import Param
import requests
import pandas as pd


class Data:

    params = None
    info = None
    
    def __init__(self,lat, long):
        self.params =  {
    "latitude": lat,
    "longitude": long,
    "current_weather": "true",
    "temperature_unit": "fahrenheit"
}
        
    #
    url = "https://api.open-meteo.com/v1/forecast"

    def getCurrentWeather(self):
        # returns the dictionary for current weather
        self.response = requests.get(self.url, params=self.params)
        data = self.response.json()
        return data.get('current_weather', None)
    #
    def display_Weather(self):
        #Prints current weather conditions for given Location
        weather_data = self.getCurrentWeather()
        
        if weather_data:
            print(f"{weather_data}")
        else:
            print("Failed to retrieve weather data.")
    #






