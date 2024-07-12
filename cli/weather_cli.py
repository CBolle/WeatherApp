from commands.command import Command

class WeatherCLI:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, city_name: str, command_name: str):
        if command_name in self.commands:
            return self.commands[command_name].execute()
        else:
            print(f"Command {command_name} not recognized.")