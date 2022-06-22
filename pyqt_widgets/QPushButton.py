from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,900,600) # (x,y,w,h)

        # set title and icon for window
        self.setWindowTitle("PushButton")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))
        # change bg color and transeparancy:
        self.setStyleSheet('background-color:orange')

        self.create_button(name='kill')

    def create_button(self, name="click",
                      Geo=(100,100,110,40),
                      color='red',
                      font_size = 14,
                      icon_img = "images/red_snake.jpg",
                      icon_size = (36,36)
                      ):
        """
        this method create button
        """

        btn = QPushButton(name, self)
        btn.setGeometry(*Geo)
        btn.setFont(QFont("time", font_size, QFont.Weight.Bold))
        btn.setStyleSheet(f'color:{color}')
        btn.setIcon(QIcon(icon_img))
        btn.setIconSize(QSize(*icon_size))

        # popup menu
        menu = QMenu()
        menu.setStyleSheet('background-color:brown')
        menu.addAction("byGun")
        menu.addAction("byKnife")
        menu.addAction("byPoison")
        btn.setMenu(menu)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
