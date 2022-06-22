from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
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

        btn1 = self.create_button(name='kill_by_knife')
        btn2 = self.create_button(name='kill_by_poison')
        btn3 = self.create_button(name='kill_by_gun')

        grid = QGridLayout()
        grid.addWidget(btn1,0,0)
        grid.addWidget(btn2,0,3)
        grid.addWidget(btn3,1,2)

        self.setLayout(grid)

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

        btn = QPushButton(name)
        btn.setGeometry(*Geo)
        btn.setFont(QFont("time", font_size, QFont.Weight.Bold))
        btn.setStyleSheet(f'color:{color}')
        btn.setIcon(QIcon(icon_img))
        btn.setIconSize(QSize(*icon_size))

        return btn


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
