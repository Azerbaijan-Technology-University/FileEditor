from dataclasses import dataclass
from pathlib import Path


@dataclass
class CommandData:
    arguments: list[str]
    commands: list["Command"]
    cwd: Path


class Command:
    def names(self) -> list[str]:
        return []

    def description(self) -> str:
        return ""

    def run(self, data: CommandData) -> None:
        pass
