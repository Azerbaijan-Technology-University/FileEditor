from pathlib import Path
from time import sleep

from pathvalidate import is_valid_filepath

from command import Command, CommandData
from terminal_editor import open_terminal_editor


def edit_file(data: CommandData):
    if len(data.arguments) < 1 or not data.arguments[0].strip():
        print(
            "Provide file name as second argument (Relative to current wroking directory)."
        )
        return

    if not is_valid_filepath(data.arguments[0]):
        print("File path is not valid.")
        return

    current_file = Path(data.arguments[0])

    print(f"Editing '{current_file.resolve()}' in 3 seconds.")
    print("Press Ctrl + S to save.")
    print("Press Ctrl + Q to quit.")
    sleep(3)
    open_terminal_editor(current_file)


edit_command = Command(["Edit", "Open"], "Create/Edit file", edit_file)
