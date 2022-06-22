from PyQt6.QtWidgets import QApplication, QWidget,QTableWidget,QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,700,400) # (x,y,w,h)

        # set title and icon for window
        self.setWindowTitle(" QTableWidget")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))
        table = QTableWidget()
        table.setRowCount(5)
        table.setColumnCount(2)
        table.setItem(0,0,QTableWidgetItem("id"))
        table.setItem(0,1,QTableWidgetItem("name"))

        vbox = QVBoxLayout()
        vbox.addWidget(table)
        self.setLayout(vbox)



app = QApplication(sys.argv)

#window = QWidget()
window = Window()

window.show()

sys.exit(app.exec())
