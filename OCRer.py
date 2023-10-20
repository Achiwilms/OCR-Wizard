import os, sys 
import ocrmypdf
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtCore import QTimer
from Ender import Ender
import time

class OCRer(QWidget):
    def __init__(self, LanguageSelector=None):
        super().__init__()    
        
        # set the language selector
        self.LanguageSelector = LanguageSelector

        # Set the window title
        self.setWindowTitle('OCR Wizard')
        # Set the window size
        self.setGeometry(100, 100, 1000, 600)

        # Create a button to select file
        self.word_label = QLabel('OCR in progress', self)

        # Create a layout to add checkboxes and the buttons
        layout = QVBoxLayout()

        # Add the button to the layout
        layout.addWidget(self.word_label)

        # Set the layout for the main window
        self.setLayout(layout)

        # Timer to simulate progress and update the label
        # self.progress_timer = QTimer(self)
        # self.progress_timer.timeout.connect(self.simulate_progress)
        # self.progress_timer.start(1000)  

        # start OCR process
        self.ocr_process()

    def simulate_progress(self):
        # Simulate progress by updating the label text
        current_text = self.word_label.text()
        if current_text.endswith('...') or current_text.endswith('document'):
            current_text = 'OCR in progress'
        else:
            current_text += '.'
        self.word_label.setText(current_text)

    def ocr_process(self):
        # ocr all pdf files
        # for file_path in self.LanguageSelector.FileSelector.file_paths:
        #     dir, filename = os.path.split(file_path)
        #     output_path = os.path.join(dir, f"OCR_{filename}")
        #     ocrmypdf.ocr(file_path, output_path, language=self.LanguageSelector.selected_languages)

        # # complete message
        # print(f"OCR completed for {len(self.file_paths)} files.")            
        
        # # clear file paths
        # self.FileSelector.file_paths = []
        # time.sleep(3)

        
        # close this window
        self.close()

        # Open the ending window 
        self.progress_window = Ender()
        self.progress_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OCRer()
    window.show()
    sys.exit(app.exec_())