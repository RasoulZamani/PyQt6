from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QLineEdit
from PyQt6.QtGui import QIcon,QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,700,400) # (x,y,w,h)
        # set title and icon for window
        self.setWindowTitle("PyQt6- event handling")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))

        self.create_widget()


    def create_widget(self):
        grid = QGridLayout()
        btn = QPushButton("save changed txt")
        btn.clicked.connect(self.btn_clicked)
        self.label = QLabel("txt")
        self.label.setStyleSheet('color:green')
        self.label.setFont(QFont('Times',19))
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("enter txt here")


        grid.addWidget(btn,2,3)
        grid.addWidget(self.label,1,2)
        grid.addWidget(self.line_edit,0,1)

        self.setLayout(grid)

    def btn_clicked(self):
        new_txt = self.line_edit.text()
        self.label.setText(new_txt)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
