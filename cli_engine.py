from pathlib import Path

from command import Command, CommandData


class CliEngine:
    def __init__(self) -> None:
        self.commands: list[Command] = []
        self.cwd = Path.cwd()

    def add_command(self, cmd: Command) -> "CliEngine":
        self.commands.append(cmd)
        return self

    def run(self) -> None:
        while True:
            user_input = input("File editor> ").split(" ")
            command_map = {
                name.lower(): cmd for cmd in self.commands for name in cmd.names()
            }

            command = user_input[0].lower()

            if command in command_map:
                command_map[command].run(
                    CommandData(user_input[1:], self.commands, self.cwd)
                )
            else:
                print("Command not found, use help command to see list of commands.")
