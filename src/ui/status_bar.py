from PySide6.QtWidgets import QStatusBar


class StudioStatusBar(QStatusBar):

    def __init__(self):
        super().__init__()

        self.showMessage("Ready")