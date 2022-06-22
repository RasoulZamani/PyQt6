from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,900,600) # (x,y,w,h)

        # set title and icon for window
        self.setWindowTitle("SNAKE")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))

        # you can fix size :
        #self.setFixedWidth(700)
        #self.setFixedHeight(400)

        # change bg color and transeparancy:
        self.setStyleSheet('background-color:yellow')
        #self.setWindowOpacity(0.95)


        # adding text label and set position and font
        label_txt = QLabel("this snake will kill you!ha ha ha!!", self)
        label_txt.move(15,20)
        label_txt.setFont(QFont('Sanserif',20))
        label_txt.setStyleSheet('color:red')

        # adding image by QLabel
        label_img = QLabel(self)
        label_img.move(20,60)
        img = QPixmap("images/red_snake.jpg")
        label_img.setPixmap(img)

        # adding gif:  without sound
        label_gif = QLabel(self)
        label_gif.move(500,100)
        gif = QMovie("images/sky.gif")
        gif.setSpeed(500)
        label_gif.setMovie(gif)
        gif.start()


app = QApplication(sys.argv)

#window = QWidget()
window = Window()

window.show()

sys.exit(app.exec())
