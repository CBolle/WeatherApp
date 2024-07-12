from services.weather_service import WeatherService
from services.external_weather_api import ExternalWeatherAPI

class WeatherServiceAdapter(WeatherService):
    def __init__(self, external_api: ExternalWeatherAPI, city):
        self.external_api = external_api
        self.city = city

    def get_current_weather(self):
        data = self.external_api.fetch_current(self.city)
        # Convert data to the required format if necessary
        return data

    def get_weather_forecast(self):
        data = self.external_api.fetch_forecast(self.city)
        # Convert data to the required format if necessary
        return data