import json
from pathlib import Path

from src.models.project import Project


class ProjectService:

    def create(self, base_path: Path, name: str) -> Project:

        project_path = base_path / name

        folders = [
            "assets",
            "thumbnail",
            "music",
            "image",
            "video",
            "export",
            "cache",
        ]

        project_path.mkdir(parents=True, exist_ok=True)

        for folder in folders:
            (project_path / folder).mkdir(exist_ok=True)

        project = Project(
            name=name,
            root=project_path,
        )

        with open(
            project_path / "project.vps",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(project.to_dict(), f, indent=4)

        return project