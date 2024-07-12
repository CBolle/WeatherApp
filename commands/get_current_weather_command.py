from services.weather_service import WeatherService
from commands.command import Command

class GetCurrentWeatherCommand(Command):
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service
        self.request_type = "current"

    def execute(self, city):
        return self.weather_service.get_weather(city, self.request_type)