# PyQt6

It is a free library in python for creating **Graphical User Interface (GUI)** based on Qt in C++.
*****
I start from implementing elementary widgets:
QLabel : for showing label text
QPushButton: simple button
QLineEdit: user can write on it
QSpinBox: increase/decrease or re-asign value
QTable: creating table
QGridLayout: enable adding widget gridly
QInputDialog: getting text, num or item from user

I gather together them in [this folder](pyqt_widgets).

*****

Then I try to create simple node pad as a self defined project. you can see codes in
[this filder](notePad_Project).
I separate design code and functionalities in two file. 
this application has menubar including file,edit,format,help and many actions like save, open, new, print and...
 
for running go to directory contain both codes i.e:
 [note_pad_design.py]("notePad_Project\note_pad_design.py") and [note_pad.py]("notePad_Project\note_pad.py")
manually or by:
```
cd notePad_Project
```

and then run note_pad.py :

```
python note_pad.py
```