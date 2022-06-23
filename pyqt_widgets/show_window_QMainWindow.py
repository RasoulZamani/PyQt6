from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("wellcome Home")
window.menuBar().addMenu("File")
window.menuBar().addMenu("Tools")
window.menuBar().addMenu("Help")
window.setCentralWidget(QLabel("hiiii"))

window.show()

sys.exit(app.exec())
