from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout


class Workspace(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel(
            "Welcome to\n\n"
            "VRUNELLO Python Studio\n\n"
            "No Project Opened"
        )

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)