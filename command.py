from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass
class CommandData:
    arguments: list[str]
    commands: list["Command"]
    cwd: Path


@dataclass
class Command:
    name: list[str]
    description: str
    action: Callable[[CommandData], None]
