from services.weather_service import WeatherService
from commands.command import Command

class GetWeatherForecastCommand(Command):
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service

    def execute(self, city):
        self.city = city
        return self.weather_service.get_weather_forecast(self.city)