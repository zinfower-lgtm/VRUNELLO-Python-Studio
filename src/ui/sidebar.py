from PySide6.QtWidgets import QListWidget


class Sidebar(QListWidget):

    def __init__(self):
        super().__init__()

        self.addItems([
            "📁 Projects",
            "🖼 Assets",
            "🎵 Music",
            "🖼 Images",
            "🎬 Videos",
            "📄 Templates",
        ])