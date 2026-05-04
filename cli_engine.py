from command import Command, CommandData


class CliEngine:
    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands
        self.command_data = CommandData(commands)

    def run(self) -> None:
        while True:
            user_input = input("File editor> ")

            for command in self.commands:
                if any(name.lower() == user_input.lower() for name in command.name):
                    command.action(self.command_data)
                    break
                else:
                    print("Command not found, use help command to see all commands.")
                    break
