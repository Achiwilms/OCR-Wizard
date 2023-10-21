import sys
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog, QPushButton, QApplication
from src.LanguageSelector import LanguageSelector

class FileSelector(QWidget):
    def __init__(self):
        super().__init__()    
        
        # Set the window title
        self.setWindowTitle('OCR Wizard')
        # Set the window size
        self.setGeometry(100, 100, 1000, 600)

        # Create a button to select file
        self.word_label = QLabel('Please select one or more PDF files for OCR', self)
        self.file_button = QPushButton('Select File', self)

        # Create a layout to add checkboxes and the buttons
        layout = QVBoxLayout()

        # Add the button to the layout
        layout.addWidget(self.word_label)
        layout.addWidget(self.file_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the buttons to their respective functions
        self.file_button.clicked.connect(self.select_file)

    def select_file(self):
        self.file_paths = []
        options = QFileDialog.Options()
        all_file_paths, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "All Files (*)", options=options)
        for file_path in all_file_paths:
            if file_path.endswith(".pdf"):
                self.file_paths.append(file_path)
                # print(f"Selected file: {file_path.split('/')[-1]}")

        # check if at least one file is selected
        if len(self.file_paths) == 0:
            # error message
            self.word_label.setText("[ERROR] Please select at least one PDF file.")
            # change the font type
            self.word_label.setStyleSheet("font-size: 36px; color: red;")
            return

        # close this window
        self.close()

        # Open the language selector window and pass a reference to self
        self.progress_window = LanguageSelector(self)
        self.progress_window.show()
        return 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileSelector()
    window.show()
    sys.exit(app.exec_())