from dataclasses import dataclass
from typing import Callable


@dataclass
class CommandData:
    commands: list["Command"]


@dataclass
class Command:
    name: list[str]
    description: str
    action: Callable[[CommandData], None]
