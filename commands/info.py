from command import Command, CommandData


class InfoCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["Info", "About"]

    def description(self) -> str:
        return "Print info about this app."

    def run(self, data: CommandData) -> None:
        print("TODO! ADD INFO ABOUT APP HERE!")
