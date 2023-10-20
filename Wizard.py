import os, sys
import ocrmypdf
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication

class Wizard(QWidget):
    def __init__(self, LanguageSelector=None):
        super().__init__()    
        
        # Set the language selector
        self.LanguageSelector = LanguageSelector

        # Set the window title
        self.setWindowTitle('OCR Wizard')
        # Set the window size
        self.setGeometry(100, 100, 1000, 600)

        # Create a button to select file
        self.word_label = QLabel('OCR in progress', self)
        self.close_button = QPushButton('Close', self)

        # Create a layout to add checkboxes and the buttons
        layout = QVBoxLayout()

        # Add the button to the layout
        layout.addWidget(self.word_label)
        layout.addWidget(self.close_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the buttons to their respective functions
        self.close_button.clicked.connect(self.close_window)

    # This function is called when the window is shown
    def showEvent(self, event):
        super().showEvent(event) 
        # Start OCR
        self.ocr_process()

    def ocr_process(self):
        # ocr all pdf files
        for file_path in self.LanguageSelector.FileSelector.file_paths:
            dir, filename = os.path.split(file_path)
            output_path = os.path.join(dir, f"OCR_{filename}")
            ocrmypdf.ocr(file_path, output_path, language=self.LanguageSelector.selected_languages)

        # complete message
        # print(f"OCR completed for {len(self.LanguageSelector.FileSelector.file_paths)} files.") 
        self.word_label.setText("Successfully OCR all files 🎉🎉🎉")           
        
    def close_window(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ender()
    window.show()
    sys.exit(app.exec_())