import sys

from command import Command, CommandData


class ExitCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["Quit", "Exit"]

    def description(self) -> str:
        return "exit app"

    def run(self, data: CommandData) -> None:
        sys.exit(0)
