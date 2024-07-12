import requests
import json
import urllib.parse

from configparser import ConfigParser

class ExternalWeatherAPI:
    def __init__(self):
        self.api_key = self._get_api_key()
        self.base_url = "https://api.openweathermap.org/data/2.5"

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
            raise NotImplementedError("The 'overview' request type is not implemented yet.")

        return self.url

    def fetch(self, city, request_type):
        try:
            response = requests.get(self.link(city, request_type))
            response.raise_for_status()

            json_object = response.json()
            main = json_object['main']
            temp = main['temp']
            return f"The temperature in {city} is {temp} degrees Celsius at the moment"
        
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            if response.status_code == 401:
                return f"Error 401: Unauthorized access. {http_err}"
            elif response.status_code == 403:
                return f"Error 403: Forbidden access. {http_err}"
            elif response.status_code == 404:
                return f"Error 404: Resource not found. {http_err}"
            else:
                return f"HTTP error occurred: {http_err}"
        except requests.exceptions.ConnectionError as conn_err:
            # Handle connection errors
            return f"Connection error occurred: {conn_err}"
        except requests.exceptions.Timeout as timeout_err:
            # Handle timeout errors
            return f"Timeout error occurred: {timeout_err}"
        except requests.exceptions.RequestException as req_err:
            # Handle any other request exceptions
            return f"An error occurred: {req_err}"
        
       