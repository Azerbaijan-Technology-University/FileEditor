import sys

from command import Command, CommandData


def exit_app(data: CommandData):
    sys.exit(0)


exit_command = Command(["Quit", "Exit"], "exit app", exit_app)
