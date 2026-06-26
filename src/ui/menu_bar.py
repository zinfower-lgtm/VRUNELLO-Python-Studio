from PySide6.QtGui import QAction


class StudioMenu:

    def __init__(self, window):

        menu = window.menuBar()

        file_menu = menu.addMenu("File")
        edit_menu = menu.addMenu("Edit")
        project_menu = menu.addMenu("Project")
        ai_menu = menu.addMenu("AI")
        tools_menu = menu.addMenu("Tools")
        help_menu = menu.addMenu("Help")

        file_menu.addAction(QAction("New Project", window))
        file_menu.addAction(QAction("Open", window))
        file_menu.addSeparator()
        file_menu.addAction(QAction("Exit", window))
        new_action = QAction("New Project", window)
        new_action.triggered.connect(window.new_project)

        file_menu.addAction(new_action)
        from src.services.project_service import ProjectService
        from src.ui.new_project_dialog import NewProjectDialog