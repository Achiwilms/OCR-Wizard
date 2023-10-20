import sys
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

        self.dynamic_button = QPushButton('Dynamic Button', self)
        self.dynamic_button.clicked.connect(self.dynamic_button_clicked)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.progress_label)
        self.layout().addWidget(self.close_button)
        self.layout().addWidget(self.dynamic_button)
        self.ocr_in_progress = True

    def close_window(self):
        self.close()
        parent = self.parent
        parent.show()

    def dynamic_button_clicked(self):
        self.progress_label.setText('Dynamic Button Clicked!')

class LanguageSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OCR Wizard')
        self.setGeometry(100, 100, 300, 100)

        self.start_ocr_button = QPushButton('Start OCR', self)
        self.start_ocr_button.clicked.connect(self.start_ocr)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.start_ocr_button)

        self.word_label = QLabel('Hello', self)
        self.layout.addWidget(self.word_label)

        self.setLayout(self.layout)

        self.progress_window = None

    def start_ocr(self):
        self.hide()
        self.progress_window = OCRProgressWindow(self)
        self.progress_window.show()
        self.progress_window.ocr_in_progress = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LanguageSelector()
    window.show()
    sys.exit(app.exec_())
