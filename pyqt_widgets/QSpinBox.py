from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QLabel, QSpinBox
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,700,400) # (x,y,w,h)

        # set title and icon for window
        self.setWindowTitle("python GUI for spinbox")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))

        self.good = QLabel("lapTop Price ($)")
        self.price = QLineEdit()
        self.number=QSpinBox()
        self.number.valueChanged.connect(self.update_price)
        self.total_price = QLabel("total_price")


        hbox = QHBoxLayout()
        hbox.addWidget(self.good)
        hbox.addWidget(self.price)
        hbox.addWidget(self.number)
        hbox.addWidget(self.total_price)
        self.setLayout(hbox)

    def update_price(self):
        if self.price.text() != '':
            pr = int(self.price.text())
            num= int(self.number.text())
            self.total_price.setText(str(pr * num))
        else:
            self.total_price.setText("invlaid price")


app = QApplication(sys.argv)

#window = QWidget()
window = Window()

window.show()

sys.exit(app.exec())
