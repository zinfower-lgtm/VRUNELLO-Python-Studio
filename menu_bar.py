new_action = QAction("New Project", window)
new_action.triggered.connect(window.new_project)

file_menu.addAction(new_action)