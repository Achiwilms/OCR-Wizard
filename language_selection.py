import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton
from open_file import open_file_dialog

class LanguageSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Selection")
        self.setGeometry(100, 100, 1000, 500)
        self.languages = ["English", "Spanish", "French", "German"]
        self.open_file = open_file_dialog
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.language_checkboxes = []

        for language in self.languages:
            checkbox = QCheckBox(language)
            layout.addWidget(checkbox)
            self.language_checkboxes.append(checkbox)

        file_button = QPushButton("Choose files")
        file_button.clicked.connect(self.open_file)
        layout.addWidget(file_button)

        update_button = QPushButton("Update Languages")
        update_button.clicked.connect(self.update_languages)
        layout.addWidget(update_button)

        self.setLayout(layout)

    def update_languages(self):
        selected_languages = [checkbox.text() for checkbox in self.language_checkboxes if checkbox.isChecked()]
        print("Selected Languages:", selected_languages)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LanguageSelection()
    window.show()
    sys.exit(app.exec_())
