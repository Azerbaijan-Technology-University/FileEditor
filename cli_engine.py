from pathlib import Path
from typing import Type

from command import Command, CommandData


class CliEngine:
    def __init__(self) -> None:
        self.commands: dict[str, Command] = {}
        self.cwd = Path.cwd()

    def add_command(self, cmd: Type[Command]) -> "CliEngine":
        instance = cmd()
        for name in instance.names():
            self.commands[name.lower()] = instance
        return self

    def run(self) -> None:
        while True:
            user_input = input("File editor> ").split(" ")
            user_command = user_input[0].lower()
            command = self.commands.get(user_command)
            commands = list(set(self.commands.values()))

            if command:
                command.run(CommandData(user_input[1:], commands, self.cwd))
                continue
            else:
                print(
                    f"Command `{user_command}` not found, use help command to see list of commands."
                )
