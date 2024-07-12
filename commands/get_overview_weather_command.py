from services.weather_service import WeatherService
from commands.command import Command

class GetWeatherOverviewCommand(Command):
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service
        self.request_type = "overview"

    def execute(self, city):
        return self.weather_service.get_weather(city, self.request_type)