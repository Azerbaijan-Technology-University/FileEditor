from cli_engine import CliEngine
from commands.clear import ClearCommand
from commands.delete import DeleteCommand
from commands.edit import EditCommand
from commands.exit import ExitCommand
from commands.help import HelpCommand
from commands.info import InfoCommand
from commands.list import ListCommand
from commands.rename import RenameCommand


def main() -> None:
    cli_engine = (
        CliEngine()
        .add_command(HelpCommand)
        .add_command(EditCommand)
        .add_command(RenameCommand)
        .add_command(DeleteCommand)
        .add_command(ListCommand)
        .add_command(ClearCommand)
        .add_command(InfoCommand)
        .add_command(ExitCommand)
    )
    cli_engine.run()


if __name__ == "__main__":
    main()
