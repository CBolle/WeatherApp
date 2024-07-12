from services.external_weather_api import ExternalWeatherAPI
from services.weather_service_adapter import WeatherServiceAdapter
from commands.get_current_weather_command import GetCurrentWeatherCommand
from commands.get_forecast_weather_command import GetWeatherForecastCommand
from cli.weather_cli import WeatherCLI

def main():
    # Instantiate the external API and the adapter
    external_api = ExternalWeatherAPI()
    weather_service = WeatherServiceAdapter(external_api)

    # Create commands
    current_weather_command = GetCurrentWeatherCommand(weather_service)
    forecast_command = GetWeatherForecastCommand(weather_service)

    # Set up the CLI
    cli = WeatherCLI()
    cli.register_command('current', current_weather_command)
    cli.register_command('forecast', forecast_command)

    # Set up the command
    city = input("Please enter your location: ")
    command = input("Would you like the current weather or the forecast? (current/forecast): ")


    # Simulate executing commands
    print(cli.execute_command(city, command))

if __name__ == "__main__":
    main()
