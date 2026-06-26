from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
)


class NewProjectDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Project")

        self.name = QLineEdit()

        layout = QFormLayout(self)

        layout.addRow("Project Name", self.name)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)