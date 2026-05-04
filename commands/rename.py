import os
from pathlib import Path

from pathvalidate import is_valid_filepath

from command import Command, CommandData


def rename_file(data: CommandData):
    if len(data.arguments) < 1:
        print(
            "Provide file name [from] as second argument (Relative to current wroking directory)."
        )
        return

    if len(data.arguments) < 2:
        print("Provide file name [to] as second argument.")
        return

    from_path = Path(data.arguments[0])
    to_path = Path(data.arguments[1])

    if not from_path.exists():
        print("File does not exist.")
        return

    if not is_valid_filepath(to_path):
        print("File path is not valid.")
        return

    os.rename(from_path, to_path)


rename_command = Command(
    ["Rename"], "Rename file (Relative to current wroking directory)", rename_file
)
