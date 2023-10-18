import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

def open_file_dialog():
    app = QApplication(sys.argv)

    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Optional: Set to make the selected file read-only

    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFiles)  # Allow the user to select multiple existing files
    file_dialog.setViewMode(QFileDialog.List)  # Use a list view for a modern interface

    file_paths, _ = file_dialog.getOpenFileNames(None, "Select Files", "", "All Files (*);;Text Files (*.txt)", options=options)

    if file_paths:
        return file_paths
    else:
        return None

if __name__ == '__main__':
    selected_files = open_file_dialog()
    if selected_files:
        print("Selected files:")
        for file_path in selected_files:
            print(file_path)
    else:
        print("No files selected.")