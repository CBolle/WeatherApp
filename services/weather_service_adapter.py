from services.weather_service import WeatherService
from services.external_weather_api import ExternalWeatherAPI

class WeatherServiceAdapter(WeatherService):
    def __init__(self, external_api: ExternalWeatherAPI):
        self.external_api = external_api

    def get_weather(self, city, request_type):
        data = self.external_api.fetch(city, request_type)
        return data
    


