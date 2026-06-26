from pathlib import Path

from src.services.project_service import ProjectService


class ProjectController:

    def __init__(self):

        self.service = ProjectService()

    def create_project(self, name: str):

        return self.service.create(
            Path("projects"),
            name,
        )