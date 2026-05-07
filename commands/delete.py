import os
from pathlib import Path

from command import Command, CommandData


class DeleteCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["Delete", "Remove", "RM"]

    def description(self) -> str:
        return "Delete file"

    def run(self, data: CommandData) -> None:
        if len(data.arguments) < 1 or not data.arguments[0].strip():
            print(
                "Provide file name as second argument (Relative to current wroking directory)."
            )
            return

        current_file = Path(data.arguments[0])

        if not current_file.exists():
            print("File does not exist.")
            return

        if input("Are you sure? [Yes, Y] ").lower() in ["yes", "y"]:
            os.remove(current_file)
        else:
            print("Cancelling operation...")
