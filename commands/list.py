from command import Command, CommandData


class ListCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def names(self) -> list[str]:
        return ["List", "LS", "DIR"]

    def description(self) -> str:
        return "Print list of files in current directory"

    def run(self, data: CommandData) -> None:
        for entry in data.cwd.iterdir():
            if entry.is_dir():
                print(f"{entry.name}/")

        for entry in data.cwd.iterdir():
            if entry.is_file():
                print(entry.name)
