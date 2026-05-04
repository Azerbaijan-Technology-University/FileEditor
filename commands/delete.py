import os
from pathlib import Path

from command import Command, CommandData


def delete_file(data: CommandData):
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


delete_command = Command(["Delete", "Remove", "RM"], "Delete file", delete_file)
