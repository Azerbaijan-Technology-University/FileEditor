from pathlib import Path

from command import Command, CommandData


class CliEngine:
    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands
        self.cwd = Path.cwd()

    def run(self) -> None:
        while True:
            user_input = input("File editor> ").split(" ")
            command_map = {
                name.lower(): cmd for cmd in self.commands for name in cmd.name
            }

            command = user_input[0].lower()

            if command in command_map:
                command_map[command].action(
                    CommandData(user_input[1:], self.commands, self.cwd)
                )
            else:
                print("Command not found, use help command to see list of commands.")
