import os
import sys
import ocrmypdf
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QFileDialog

class LanguageSelector(QWidget):
    def __init__(self):
        super().__init__()    
        self.setWindowTitle('OCR Wizard')
        self.setGeometry(100, 100, 1000, 600)
        self.languages = ["English", "Traditional Chinese", "Simplified Chinese", "German", "Japanese"]
        self.languages_name = ["English", "繁體中文", "简体中文", "Deutsch", "日本語"]
        self.languages_code = ["eng", "chi_tra", "chi_sim", "deu", "jpn"]

        # Create checkboxes for different languages
        self.language_checkboxes = []
        for language_name in self.languages_name:
            checkbox = QCheckBox(language_name, self)
            self.language_checkboxes.append(checkbox)

        # Create a button to select a file and Start OCR
        self.file_button = QPushButton('Select File', self)
        self.ocr_button = QPushButton('Start OCR', self)

        # Create a layout to add checkboxes and the buttons
        layout = QVBoxLayout()

        # Add the checkboxes to the layout
        for checkbox in self.language_checkboxes:
            layout.addWidget(checkbox)    
        layout.addWidget(self.file_button)
        layout.addWidget(self.ocr_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the buttons to their respective functions
        self.file_button.clicked.connect(self.select_file)
        self.ocr_button.clicked.connect(self.start_ocr)

    def language_selected(self):
        self.selected_languages = []
        for idx, checkbox in enumerate(self.language_checkboxes):
            if checkbox.isChecked():
                self.selected_languages.append(self.languages_code[idx])
        return        

    def select_file(self):
        self.file_paths = []
        options = QFileDialog.Options()
        self.file_paths, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "All Files (*)", options=options)
        return 

    def start_ocr(self):
        self.language_selected()
        print(self.selected_languages)
        if self.file_paths:
            for file_path in self.file_paths:
                dir, filename = os.path.split(file_path)
                output_path = os.path.join(dir, f"OCR_{filename}")
                ocrmypdf.ocr(file_path, output_path, language=self.selected_languages)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LanguageSelector()
    window.show()
    sys.exit(app.exec_())

