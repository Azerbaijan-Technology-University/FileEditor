from command import Command, CommandData


def print_help_message(data: CommandData):
    print("List of commands:")
    for command in data.commands:
        name = ", ".join(command.name)
        print(f"{name} - {command.description}")


help_command = Command(["Help"], "Print this message", print_help_message)
