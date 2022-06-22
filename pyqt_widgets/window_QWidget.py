from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,700,400) # (x,y,w,h)

        # set title and icon for window
        self.setWindowTitle("python GUI titile")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))

        # you can fix size :
        #self.setFixedWidth(700)
        #self.setFixedHeight(400)

        # change bg color and transeparancy:
        self.setStyleSheet('background-color:orange')
        self.setWindowOpacity(0.95)



app = QApplication(sys.argv)

#window = QWidget()
window = Window()

window.show()

sys.exit(app.exec())
