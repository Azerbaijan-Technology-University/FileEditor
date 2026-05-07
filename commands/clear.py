import os

from command import Command, CommandData


class ClearCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["Clear", "CLS"]

    def description(self) -> str:
        return "Clear console"

    def run(self, data: CommandData) -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
