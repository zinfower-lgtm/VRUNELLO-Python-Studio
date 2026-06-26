from dataclasses import dataclass, asdict, field
from pathlib import Path
from datetime import datetime


@dataclass
class Project:
    name: str
    root: Path

    version: str = "0.1.2"

    created: str = field(default_factory=lambda: datetime.now().isoformat())
    modified: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        data = asdict(self)
        data["root"] = str(self.root)
        return data