from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,700,400) # (x,y,w,h)

        # set title and icon for window
        self.setWindowTitle(" Calender")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))
        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self.selected_date)
        self.label = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def selected_date(self):
        date = self.calendar.selectedDate()
        date_str = str(date.toPyDate())
        self.label.setText(date_str)




app = QApplication(sys.argv)

#window = QWidget()
window = Window()

window.show()

sys.exit(app.exec())
