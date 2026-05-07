from command import Command, CommandData


class ChangeDirectoryCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["Change-Directory", "cd"]

    def description(self) -> str:
        return "Change current working directory."

    def run(self, data: CommandData) -> None:
        raise Exception("Not implemented")
