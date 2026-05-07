from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CommandData:
    arguments: list[str]
    commands: list["Command"]
    cwd: Path


class Command(ABC):
    @abstractmethod
    def names(self) -> list[str]:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def run(self, data: CommandData) -> None:
        pass
