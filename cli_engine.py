from pathlib import Path

from command import Command, CommandData


class CliEngine:
    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands
        self.cwd = Path.cwd()

    def run(self) -> None:
        while True:
            user_input = input("File editor> ")
            command_map = {
                name.lower(): cmd for cmd in self.commands for name in cmd.name
            }

            if user_input in command_map:
                command_map[user_input].action(CommandData(self.commands, self.cwd))
            else:
                print("Command not found, use help command to see list of commands.")
