import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFileDialog, QPushButton, QApplication

class FileSelector(QWidget):
    def __init__(self):
        super().__init__()    
        
        # Set the window title
        self.setWindowTitle('OCR Wizard')
        # Set the window size
        self.setGeometry(100, 100, 1000, 600)

        # Create a button to select a file and Start OCR
        self.file_button = QPushButton('Select File', self)

        # Create a layout to add checkboxes and the buttons
        layout = QVBoxLayout()

        # Add the button to the layout
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
        return 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileSelector()
    window.show()
    sys.exit(app.exec_())