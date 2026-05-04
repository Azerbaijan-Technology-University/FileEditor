from cli_engine import CliEngine
from command import Command
from commands.help import help_command
from commands.list import list_command

commands: list[Command] = [help_command, list_command]


def main() -> None:
    cli_engine = CliEngine(commands)
    cli_engine.run()


if __name__ == "__main__":
    main()
