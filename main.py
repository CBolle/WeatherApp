from services.external_weather_api import ExternalWeatherAPI
from services.weather_service_adapter import WeatherServiceAdapter
from commands.get_current_weather_command import GetCurrentWeatherCommand
from commands.get_overview_weather_command import GetWeatherOverviewCommand
from cli.weather_cli import WeatherCLI

def main():
    # Instantiate the external API and the adapter
    external_api = ExternalWeatherAPI()
    weather_service = WeatherServiceAdapter(external_api)

    # Create commands
    current_weather_command = GetCurrentWeatherCommand(weather_service)
    overview_command = GetWeatherOverviewCommand(weather_service)

    # Set up the CLI
    cli = WeatherCLI()
    cli.register_command('current', current_weather_command)
    cli.register_command('overview', overview_command)

    # Set up the command
    city = input("City: ")
    command = input("Would you like the current weather or the overview? (current/overview): ")


    # Simulate executing commands
    print(cli.execute_command(city, command))

if __name__ == "__main__":
    main()
