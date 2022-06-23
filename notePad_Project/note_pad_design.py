""" ************ In His High Name ************
 In this project we create simple (but still
awsome!) node pat in PyQt6

           By Rasoul Zamani
                1401/04

        you can use it for free!
"""

from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QTextEdit, QVBoxLayout,
                             QToolBar)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("my Note Pad")
        self.setGeometry(300,300,700,500)
        self.statusBar().showMessage("wellcome to awsome note pad! type anything you like!its free:)")

        self._createActions()
        self._createMenuBar()
        self._create_toolbar()

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

# actions ______________________________________________________________________
    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setIcon(QIcon("icon_images/new.png"))
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setIcon(QIcon("icon_images/open.png"))
        self.saveAction = QAction("&Save", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setIcon(QIcon("icon_images/save.png"))
        self.printAction = QAction("&Print", self)
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.setIcon(QIcon("icon_images/print.png"))
        self.printPreviewAction = QAction("&Print Preview", self)
        self.printPreviewAction.setShortcut("Ctrl+Shift+P")
        self.printPreviewAction.setIcon(QIcon("icon_images/printprev.png"))
        self.exportAction = QAction("&Export", self)
        self.exportAction.setShortcut("Ctrl+E")
        self.exportAction.setIcon(QIcon("icon_images/pdf.png"))
        self.quitAction = QAction("&Quit", self)
        self.quitAction.setShortcut("Ctrl+Q")
        self.quitAction.setIcon(QIcon("icon_images/exit.png"))

        self.undoAction = QAction("&Undo", self)
        self.undoAction.setIcon(QIcon("icon_images/undo.png"))
        self.redoAction = QAction("&Redo", self)
        self.redoAction.setIcon(QIcon("icon_images/redo.png"))
        self.cutAction = QAction("&Cut", self)
        self.cutAction.setIcon(QIcon("icon_images/cut.png"))
        self.copyAction = QAction("&Copy", self)
        self.copyAction.setIcon(QIcon("icon_images/copy.png"))
        self.pasteAction = QAction("&Paste", self)
        self.pasteAction.setIcon(QIcon("icon_images/paste.png"))

        self.boldAction = QAction("&Bold", self)
        self.boldAction.setIcon(QIcon("icon_images/bold.png"))
        self.italicAction = QAction("&Italic", self)
        self.italicAction.setIcon(QIcon("icon_images/italic.png"))
        self.underlineAction = QAction("&Undeline", self)
        self.underlineAction.setIcon(QIcon("icon_images/underline.png"))
        self.leftAction = QAction("&Left", self)
        self.leftAction.setIcon(QIcon("icon_images/left.png"))
        self.rightAction = QAction("&Right", self)
        self.rightAction.setIcon(QIcon("icon_images/right.png"))
        self.centerAction = QAction("&Center", self)
        self.centerAction.setIcon(QIcon("icon_images/center.png"))
        self.justifyAction = QAction("&Justify", self)
        self.justifyAction.setIcon(QIcon("icon_images/justify.png"))
        self.fontAction = QAction("&Font", self)
        self.fontAction.setIcon(QIcon("icon_images/font.png"))
        self.colorAction = QAction("&Color", self)
        self.colorAction.setIcon(QIcon("icon_images/color.png"))

        self.helpAction = QAction("&Help", self)
        self.helpAction.setIcon(QIcon("icon_images/about.png"))
        self.aboutAction = QAction("&About", self)
        self.aboutAction.setIcon(QIcon("icon_images/aboutqt.png"))

# menu bar _____________________________________________________________________
    def _createMenuBar(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.printAction)
        fileMenu.addAction(self.printPreviewAction)
        fileMenu.addAction(self.exportAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.quitAction)

        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.undoAction)
        editMenu.addAction(self.redoAction)
        editMenu.addSeparator()
        editMenu.addAction(self.cutAction)
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)

        formatMenu = menuBar.addMenu("&Format")
        formatMenu.addAction(self.boldAction)
        formatMenu.addAction(self.italicAction)
        formatMenu.addAction(self.underlineAction)
        formatMenu.addSeparator()
        formatMenu.addAction(self.leftAction)
        formatMenu.addAction(self.rightAction)
        formatMenu.addAction(self.centerAction)
        formatMenu.addAction(self.justifyAction)
        formatMenu.addSeparator()
        formatMenu.addAction(self.colorAction)
        formatMenu.addAction(self.fontAction)

        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)

# toolbar ______________________________________________________________________
    def _create_toolbar(self):
        toolbar = QToolBar("My main toolbar")
        toolbar.addAction(self.newAction)
        toolbar.addAction(self.openAction)
        toolbar.addAction(self.saveAction)
        toolbar.addAction(self.undoAction)
        toolbar.addAction(self.redoAction)
        toolbar.addAction(self.helpAction)

        self.addToolBar(toolbar)



if __name__ == "__main__": #____________________________________________________
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
