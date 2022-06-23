""" ************ In His High Name ************
 In this project we create simple (but still
awsome!) node pat in PyQt6

This part (by name: note_pad.py) is for adding
functions.
another code for design is note_pad_design.py
and we import app design from it.

           By Rasoul Zamani
                1401/04

        you can use it for free!
"""
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QFileDialog, QMessageBox,
                             QFontDialog, QColorDialog)
from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtPrintSupport import QPrinter,QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt
import sys
from note_pad_design import Window as Design

class Window(Design):
    """Main Window."""
    def __init__(self):
        super().__init__()
# signals:

# signals of File _____________________________________________________
        self.saveAction.triggered.connect(self.save_file)
        self.newAction.triggered.connect(self.new_file)
        self.openAction.triggered.connect(self.open_file)
        self.printAction.triggered.connect(self.print_file)
        self.printPreviewAction.triggered.connect(self.preview_dialog)
        self.exportAction.triggered.connect(self.export_pdf)
        self.quitAction.triggered.connect(self.quit_app)

# signals of Edit ____________________________________________________
        self.undoAction.triggered.connect(self.textEdit.undo)
        self.redoAction.triggered.connect(self.textEdit.redo)
        self.cutAction.triggered.connect(self.textEdit.cut)
        self.copyAction.triggered.connect(self.textEdit.copy)
        self.pasteAction.triggered.connect(self.textEdit.paste)

# signals of Format __________________________________________________
        self.boldAction.triggered.connect(self.text_bold)
        self.italicAction.triggered.connect(self.italic)
        self.underlineAction.triggered.connect(self.underline)


        self.leftAction.triggered.connect(self.align_left)
        self.centerAction.triggered.connect(self.align_center)
        self.rightAction.triggered.connect(self.align_right)
        self.justifyAction.triggered.connect(self.justify)

        self.fontAction.triggered.connect(self.font_dialog)
        self.colorAction.triggered.connect(self.color_dialog)


        self.helpAction.triggered.connect(self.help)
        self.aboutAction.triggered.connect(self.about)

# Methods (slots) :

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

# quit from app ________________________________________________________________
    def quit_app(self):
        self.close()

# Format methods _______________________________________________________________
    def text_bold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)

    def italic(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)

    def underline(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)


    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def about(self):
        QMessageBox.about(self,"About App",
        " \t************ In His High Name ************     "+\
        "\n In this project we create simple (but still awsome!) node pat in PyQt6"+\
        "\n\t\t By Rasoul Zamani, 1401/04 \n\n\t you can use it for free!so good for you!" )

    def help(self):
        QMessageBox.about(self,"About App",
       " Really???? you need help for usinf nodepad??!! commmee onnnn !!!")

#*******************************************************************************
if __name__ == "__main__": #____________________________________________________
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
