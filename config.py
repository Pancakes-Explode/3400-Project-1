from ast import Param
import requests
import pandas as pd


class Data:

    params = None
    info = None
    lat = None
    long = None
    
    def __init__(self,lat, long):
        self.lat = lat
        self.long = long
        self.params =  {
    "latitude": lat,
    "longitude": long,
    "current": ["temperature_2m", "relative_humidity_2m", "is_day", "precipitation", "rain", "weather_code", "wind_speed_10m"],
    "temperature_unit": "fahrenheit"
}
        
    #
    url = "https://api.open-meteo.com/v1/forecast"

    def getCurrentWeather(self):
        # returns the dictionary for current weather
        self.response = requests.get(self.url, params=self.params)
        data = self.response.json()
        return pd.DataFrame(data['current'], index=[1])
    #
    def display_Weather(self):
        #Prints current weather conditions for given Location
        weather_data = self.getCurrentWeather()
        weather_data.to_csv(path_or_buf= f"output/{self.lat},{self.long}")

        
        print(f"{weather_data}")
         #






