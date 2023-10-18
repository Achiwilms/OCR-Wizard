import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QFileDialog

class LanguageSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Language Selector')
        self.setGeometry(100, 100, 1000, 500)

        # Create checkboxes for different languages
        self.english_checkbox = QCheckBox('English', self)
        self.spanish_checkbox = QCheckBox('Spanish', self)
        self.french_checkbox = QCheckBox('French', self)
        self.german_checkbox = QCheckBox('German', self)

        # Create a button to select a file
        self.file_button = QPushButton('Select File', self)
        self.ocr_button = QPushButton('Start OCR', self)

        # Create a layout to add checkboxes and the button
        layout = QVBoxLayout()
        layout.addWidget(self.english_checkbox)
        layout.addWidget(self.spanish_checkbox)
        layout.addWidget(self.french_checkbox)
        layout.addWidget(self.german_checkbox)
        layout.addWidget(self.file_button)
        layout.addWidget(self.ocr_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the checkboxes and the button to their respective functions
        self.english_checkbox.stateChanged.connect(self.language_selected)
        self.spanish_checkbox.stateChanged.connect(self.language_selected)
        self.french_checkbox.stateChanged.connect(self.language_selected)
        self.german_checkbox.stateChanged.connect(self.language_selected)
        self.file_button.clicked.connect(self.select_file)
        self.ocr_button.clicked.connect(self.start_ocr)

    def language_selected(self):
        selected_languages = []

        if self.english_checkbox.isChecked():
            selected_languages.append('English')
        if self.spanish_checkbox.isChecked():
            selected_languages.append('Spanish')
        if self.french_checkbox.isChecked():
            selected_languages.append('French')
        if self.german_checkbox.isChecked():
            selected_languages.append('German')

        print(f'Selected languages: {", ".join(selected_languages)}')

    def select_file(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "All Files (*)", options=options)
        
        if file_paths:
            for file_path in file_paths:
                print(f'Selected file: {file_path}')
        else: 
            print("No files selected.")

    def start_ocr(self):
        print("start ocr")
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LanguageSelector()
    window.show()
    sys.exit(app.exec_())
