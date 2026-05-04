from command import Command, CommandData


class CliEngine:
    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands
        self.command_data = CommandData(commands)

    def run(self) -> None:
        while True:
            user_input = input("File editor> ")
            command_map = {
                name.lower(): cmd for cmd in self.commands for name in cmd.name
            }

            if user_input in command_map:
                command_map[user_input].action(self.command_data)
