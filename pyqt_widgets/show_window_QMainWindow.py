from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("wellcome Home")
window.menuBar().addMenu("File")
window.menuBar().addMenu("Tools")
window.menuBar().addMenu("Help")


window.show()

sys.exit(app.exec())
