import sys
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QApplication

class Ender(QWidget):
    def __init__(self):
        super().__init__()    
        
        # Set the window title
        self.setWindowTitle('OCR Wizard')
        # Set the window size
        self.setGeometry(100, 100, 1000, 600)

        # Create a button to select file
        self.word_label = QLabel('Successfully OCR all files!', self)
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

    def close_window(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ender()
    window.show()
    sys.exit(app.exec_())