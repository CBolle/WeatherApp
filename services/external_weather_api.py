import requests
import json
import urllib.parse

from configparser import ConfigParser

class ExternalWeatherAPI:
    def __init__(self):
        self.api_key = self._get_api_key()
        self.base_url = "https://api.openweathermap.org/data/2.5"
        print(self.api_key)

    def _get_api_key(self):
        config = ConfigParser()
        config.read("secrets.ini")
        return config["openweather"]["api_key"]
    
    def _get_encoded_api_key(self):
        a = self._get_api_key()
        encoded_key = urllib.parse.quote(a, safe='')
        return encoded_key


    def link(self, city, request_type):
        if request_type == "current":
            self.url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units=metric"

        elif request_type == "overview":
            pass
        return self.url

    def fetch(self, city, request_type):
        response = requests.get(self.link(city, request_type))
        response.raise_for_status()
        json_object = response.json()
        main = json_object['main']
        temp = main['temp']
        return f"The temperature in {city} is {temp} degrees Celsius at the moment"