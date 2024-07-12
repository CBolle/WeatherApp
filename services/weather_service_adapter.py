from services.weather_service import WeatherService
from services.external_weather_api import ExternalWeatherAPI

class WeatherServiceAdapter(WeatherService):
    def __init__(self, external_api: ExternalWeatherAPI):
        self.external_api = external_api

    def get_current_weather(self):
        data = self.external_api.fetch_current()
        # Convert data to the required format if necessary
        return data

    def get_weather_forecast(self):
        data = self.external_api.fetch_forecast()
        # Convert data to the required format if necessary
        return data