from command import Command, CommandData


class HelpCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["Help"]

    def description(self) -> str:
        return "Print this message"

    def run(self, data: CommandData) -> None:
        print("List of commands:")
        for command in data.commands:
            name = ", ".join(command.names())
            print(f"{name} - {command.description()}")
