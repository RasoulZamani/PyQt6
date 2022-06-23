from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QFileDialog, QMessageBox,
                             QLabel, QTextEdit, QVBoxLayout,
                             QToolBar)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtPrintSupport import QPrinter,QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt
import sys
from note_pad_design import Window as Design

class Window(Design):
    """Main Window."""
    def __init__(self):
        super().__init__()

        self.saveAction.triggered.connect(self.save_file)
        self.newAction.triggered.connect(self.new_file)
        self.openAction.triggered.connect(self.open_file)
        self.printAction.triggered.connect(self.print_file)
        self.printPreviewAction.triggered.connect(self.preview_dialog)
        self.exportAction.triggered.connect(self.export_pdf)
        self.quitAction.triggered.connect(self.quit_app)

        self.undoAction.triggered.connect(self.textEdit.undo)
        self.redoAction.triggered.connect(self.textEdit.redo)
        self.cutAction.triggered.connect(self.textEdit.cut)
        self.copyAction.triggered.connect(self.textEdit.copy)
        self.pasteAction.triggered.connect(self.textEdit.paste)






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

# open file ____________________________________________________________________
    def open_file(self):
        if self.save_or_not():
            file_name = QFileDialog.getOpenFileName(self,"Open File", "")
            if file_name[0]:
                f = open(file_name, 'r')
                with f:
                    doc = f.read()
                    self.textEdit.setText(data)

# print preview ________________________________________________________________
    def preview_dialog(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)
# print file ___________________________________________________________________
    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

# export pdf ___________________________________________________________________
    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export PDF', "")

        if fn != "":
            if QFileInfo(fn).suffix() == "" : fn += '.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print(printer)

# quit from app
    def quit_app(self):
        self.close()


if __name__ == "__main__": #____________________________________________________
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
