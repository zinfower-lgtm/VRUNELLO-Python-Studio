from pathlib import Path

from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
    QMessageBox,
)

from src.ui.menu_bar import StudioMenu
from src.ui.property_panel import PropertyPanel
from src.ui.sidebar import Sidebar
from src.ui.status_bar import StudioStatusBar
from src.ui.workspace import Workspace
from src.services.project_service import ProjectService
from src.ui.new_project_dialog import NewProjectDialog
from src.controllers.project_controller import ProjectController

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VRUNELLO Python Studio")
        self.resize(1600, 900)

        StudioMenu(self)

        splitter = QSplitter()

        splitter.addWidget(Sidebar())
        splitter.addWidget(Workspace())
        splitter.addWidget(PropertyPanel())

        splitter.setSizes([220, 1100, 280])

        self.setCentralWidget(splitter)

        self.setStatusBar(StudioStatusBar())
        
        self.project_controller = ProjectController()
        
    def new_project(self):

        dialog = NewProjectDialog()

        if dialog.exec():

            name = dialog.name.text().strip()

            if not name:
                return

            project = self.project_controller.create_project(name)

            QMessageBox.information(
                self,
                "Success",
                f"{project.name} created."
            )