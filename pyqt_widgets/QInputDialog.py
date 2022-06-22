from PyQt6.QtWidgets import QApplication,QPushButton, QDialog, QInputDialog, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        # set position of window
        self.setGeometry(200,200,700,400) # (x,y,w,h)

        # set title and icon for window
        self.setWindowTitle("input dialog")
        self.setWindowIcon(QIcon("images/red_snake.jpg"))

        self.creat_dialog()

    def creat_dialog(self):
        # name
        label_name = QLabel("Enter your name:")
        label_name.setFont(QFont("times",19))

        self.line_edit_name  = QLineEdit()
        self.line_edit_name.setFont(QFont("times",19))

        btn_name  = QPushButton("Enter name")
        btn_name.setFont(QFont("times",19))
        btn_name.clicked.connect(self.show_dialog_name)

        hbox_name = QHBoxLayout()
        hbox_name.addWidget(label_name)
        hbox_name.addWidget(self.line_edit_name )
        hbox_name.addWidget(btn_name )

        # country
        label_country = QLabel("Choose Country")
        label_country.setFont(QFont("times",19))

        self.line_edit_country  = QLineEdit()
        self.line_edit_country.setFont(QFont("times",19))

        btn_country  = QPushButton("Choose Country")
        btn_country.setFont(QFont("times",19))
        btn_country.clicked.connect(self.show_dialog_country)

        hbox_country = QHBoxLayout()
        hbox_country.addWidget(label_country)
        hbox_country.addWidget(self.line_edit_country )
        hbox_country.addWidget(btn_country )

        # age
        label_age = QLabel("Enter your age:")
        label_age.setFont(QFont("times",19))

        self.line_edit_age  = QLineEdit()
        self.line_edit_age.setFont(QFont("times",19))

        btn_age  = QPushButton("Enter age")
        btn_age.setFont(QFont("times",19))
        btn_age.clicked.connect(self.show_dialog_age)

        hbox_age = QHBoxLayout()
        hbox_age.addWidget(label_age)
        hbox_age.addWidget(self.line_edit_age )
        hbox_age.addWidget(btn_age )


        vbox = QVBoxLayout()
        vbox.addLayout(hbox_name)
        vbox.addLayout(hbox_country)
        vbox.addLayout(hbox_age)

        self.setLayout(vbox)

    def show_dialog_country(self):
        countries = [
        "Afghanistan","Albania","Algeria","Andorra",
        "Bahrain","Bangladesh","Barbados","Belarus"
        ]
        country, ok = QInputDialog.getItem(self,"Input Dialog","list of countries",countries, 0,False)
        if ok and country:
            self.line_edit_country.setText(country)

    def show_dialog_name(self):
        name, ok = QInputDialog.getText(self,"get name", "enter you name")
        if ok and name:
            self.line_edit_name.setText(name)

    def show_dialog_age(self):
        age, ok = QInputDialog.getInt(self,"get age", "enter you age")
        if ok and age:
            self.line_edit_age.setText(str(age))




app = QApplication(sys.argv)

#window = QWidget()
window = Window()

window.show()

sys.exit(app.exec())
