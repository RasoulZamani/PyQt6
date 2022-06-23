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
        self.newAction.triggered.connect(self.new_file)


# check save or discart:________________________________________________________
    def save_or_not(self):
        if not self.textEdit.document().isModified():
            return True
        ret = QMessageBox.warning(self, "Warning!",
             "document has been modified! \n Do you wnat to save your changes?",
             QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)

        if ret == QMessageBox.StandardButton.Save :
             return self.save_file()

        if ret == QMessageBox.StandardButton.Cancel:
            return False

        return True

# save file method _____________________________________________________________
    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File")
        if file_name[0]:
            f = open(file_name[0],'w')

            with f:
                text = self.textEdit.toPlainText()
                f.write(text)

                QMessageBox.about(self,"Save File", " File have been saved!")

# new file _____________________________________________________________________
    def new_file(self):
        if self.save_or_not():
            self.textEdit.clear()



if __name__ == "__main__": #____________________________________________________
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
