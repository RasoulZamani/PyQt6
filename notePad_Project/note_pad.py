from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QFileDialog, QMessageBox,
                             QLabel, QTextEdit, QVBoxLayout,
                             QToolBar)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys
from note_pad_design import Window as Design

class Window(Design):
    """Main Window."""
    def __init__(self):
        super().__init__()

        self.saveAction.triggered.connect(self.save_file)

    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File")
        if file_name[0]:
            f = open(file_name[0],'w')

            with f:
                text = self.textEdit.toPlainText()
                f.write(text)

                QMessageBox.about(self,"Save File", " File have been saved!")



if __name__ == "__main__": #____________________________________________________
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
