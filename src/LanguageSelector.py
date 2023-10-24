import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout, QCheckBox, QPushButton, QLabel
from src.Wizard import Wizard

class LanguageSelector(QWidget):
    def __init__(self, FileSelector=None):
        super().__init__()    
        self.FileSelector = FileSelector
        self.setWindowTitle('OCR Wizard')
        self.setGeometry(100, 100, 1000, 600)
        # ('name of language', 'language code in tesseract')
        self.languages = [
            ("English", "eng"),
            ("繁體中文", "chi_tra"),
            ("简体中文", "chi_sim"),
            ("日本語", "jpn"),
            ("Deutsch", "deu"),
            ("Español", "spa")
        ]

        # Create checkboxes for different languages
        self.language_checkboxes = []
        for language_name, _ in self.languages:
            checkbox = QCheckBox(language_name, self)
            self.language_checkboxes.append(checkbox)
        
        # Create a label for instructions
        self.word_label = QLabel('Please select the languages in the document', self)

        # Create a button to select a file and Start OCR
        self.ocr_button = QPushButton('Start OCR', self)

        # Create a layout to add checkboxes and the buttons
        layout = QVBoxLayout()

        # Add the checkboxes to the layout
        layout.addWidget(self.word_label)
        for checkbox in self.language_checkboxes:
            layout.addWidget(checkbox)   
        layout.addWidget(self.ocr_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the buttons to their respective functions
        self.ocr_button.clicked.connect(self.start_ocr)

    def language_selected(self):
        # get the selected languages
        self.selected_languages = [self.languages[idx][1] for idx, checkbox in enumerate(self.language_checkboxes) if checkbox.isChecked()]
        print(self.selected_languages)

    def start_ocr(self):
        # Call the language_selected method to update the selected_languages attribute
        self.language_selected()

        # Check if no languages are selected
        if not self.selected_languages:
            # Display an error message in the word_label widget
            self.word_label.setText("[ERROR] Please select at least one language.")
            self.word_label.setStyleSheet("font-size: 36px; color: red;")
            return

        # Close the current window
        self.close()

        # Create an instance of the Wizard class, passing in the current instance and the FileSelector attribute
        self.progress_window = Wizard(self, self.FileSelector)
        
        # Show the progress window
        self.progress_window.show()
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LanguageSelector()
    window.show()
    sys.exit(app.exec_())