import os
from pathlib import Path

from pathvalidate import is_valid_filepath

from command import Command, CommandData


class RenameCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["Rename"]

    def description(self) -> str:
        return "Rename file (Relative to current wroking directory)"

    def run(self, data: CommandData) -> None:
        if len(data.arguments) < 1 or not data.arguments[0].strip():
            print(
                "Provide file name [from] as second argument (Relative to current wroking directory)."
            )
            return

        if len(data.arguments) < 2 or not data.arguments[1].strip():
            print("Provide file name [to] as second argument.")
            return

        from_path = Path(data.arguments[0])
        to_path = Path(data.arguments[1])

        if not from_path.exists():
            print("File does not exist.")
            return

        if not is_valid_filepath(data.arguments[1]):
            print("File path is not valid.")
            return

        os.rename(from_path, to_path)
