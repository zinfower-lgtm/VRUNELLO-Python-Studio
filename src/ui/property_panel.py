from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class PropertyPanel(QLabel):

    def __init__(self):
        super().__init__("Nothing Selected")

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)