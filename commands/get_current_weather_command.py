from services.weather_service import WeatherService

class GetCurrentWeatherCommand(Command):
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service

    def execute(self):
        return self.weather_service.get_current_weather()