import os

from command import Command, CommandData


def clear_console(data: CommandData):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clear_command = Command(["Clear", "CLS"], "Clear console", clear_console)
