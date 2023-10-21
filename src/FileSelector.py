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
        # Set options for the file dialog
        options = QFileDialog.Options()

        # Open the file dialog and get the selected file paths
        all_file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Select File", "", "All Files (*)", options=options)

        # Filter the file paths to only include PDF files
        self.file_paths = [file_path for file_path in all_file_paths if file_path.endswith(".pdf")]

        # Check if at least one file is selected
        if len(self.file_paths) == 0:
            # Display an error message if no PDF files are selected
            self.word_label.setText("[ERROR] Please select at least one PDF file.")
            self.word_label.setStyleSheet("font-size: 36px; color: red;")
            return

        # Close the current window
        self.close()

        # Create and show the progress window
        self.progress_window = LanguageSelector(self)
        self.progress_window.show()
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileSelector()
    window.show()
    sys.exit(app.exec_())