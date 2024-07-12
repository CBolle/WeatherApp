from configparser import ConfigParser

class ExternalWeatherAPI:
    def _get_api_key():
        config = ConfigParser()
        config.read("secrets.ini")
        return config["openweather"]["api_key"]


    def fetch_current(self):
        # Simulate fetching data from an external API
        return {"temperature": 72, "condition": "Sunny"}

    def fetch_forecast(self):
        # Simulate fetching forecast data from an external API
        return [{"day": "Monday", "condition": "Sunny", "high": 75, "low": 65}]