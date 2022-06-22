from PyQt6.QtWidgets import (QApplication, QMainWindow,
                            QLabel)
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
        self.statusBar().showMessage("wellcome to awsome note pad")

        self._createActions()
        self._createMenuBar()

        self.centralWidget = QLabel("Hello, World")

    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setShortcut("Ctrl+N")
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction = QAction("&Save", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.printAction = QAction("&Print", self)
        self.printAction.setShortcut("Ctrl+P")
        self.exportAction = QAction("&Export", self)
        self.quitAction = QAction("&Quit", self)
        self.quitAction.setShortcut("Ctrl+Q")


        self.undoAction = QAction("&Undo", self)
        self.reduAction = QAction("&Redu", self)
        self.cutAction = QAction("&Cut", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)

        self.boldAction = QAction("&Bold", self)
        self.italicAction = QAction("&Italic", self)
        self.underlineAction = QAction("&Undeline", self)
        self.leftAction = QAction("&Left", self)
        self.rightAction = QAction("&Right", self)
        self.centerAction = QAction("&Center", self)
        self.justifyAction = QAction("&Justify", self)
        self.fontAction = QAction("&Font", self)
        self.colorAction = QAction("&Color", self)

        self.helpAction = QAction("&Help", self)
        self.aboutAction = QAction("&About", self)

    def _createMenuBar(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.printAction)
        fileMenu.addAction(self.exportAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.quitAction)

        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.undoAction)
        editMenu.addAction(self.reduAction)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
