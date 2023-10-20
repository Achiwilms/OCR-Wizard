import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class OCRProgressWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('OCR Progress')
        self.setGeometry(100, 100, 300, 100)
        self.progress_label = QLabel('OCR in progress...', self)
        self.close_button = QPushButton('Close', self)
        self.close_button.clicked.connect(self.close_window)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.progress_label)
        self.layout().addWidget(self.close_button)

    def close_window(self):
        self.close()
        self.parent.show()

class LanguageSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OCR Wizard')
        self.setGeometry(100, 100, 300, 100)

        self.start_ocr_button = QPushButton('Start OCR', self)
        self.start_ocr_button.clicked.connect(self.start_ocr)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.start_ocr_button)

    def start_ocr(self):
        # Hide the main window
        self.hide()

        # Open the OCR progress window
        self.progress_window = OCRProgressWindow(self)
        self.progress_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LanguageSelector()
    window.show()
    sys.exit(app.exec_())
