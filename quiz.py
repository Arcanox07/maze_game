from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup, QHBoxLayout


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Quiz')
main_win.move(900, 70)
main_win.resize(400, 200)
main_win.show()

button1 = QRadioButton('3')
button1.setChecked(True) 
button2 = QRadioButton('5')
button3 = QRadioButton('6')
button4 = QRadioButton('4')
checkbutton = QPushButton('Check answer')

group = QButtonGroup()
group.addButton(button1, id = 1)
group.addButton(button2, id = 2)
group.addButton(button3, id = 3)
group.addButton(button4, id = 4)



vertical = QVBoxLayout()
horizontal1 = QHBoxLayout()
horizontal2 = QHBoxLayout()
horizontal3 = QHBoxLayout()
horizontal4 = QHBoxLayout()
horizontal5 = QHBoxLayout()

question = QLabel('What is 2 + 2?')
horizontal1.addWidget(question, alignment = Qt.AlignLeft)
horizontal2.addWidget(button1, alignment = Qt.AlignLeft)
horizontal2.addWidget(button2, alignment = Qt.AlignRight)
horizontal3.addWidget(button3, alignment = Qt.AlignLeft)
horizontal3.addWidget(button4, alignment = Qt.AlignRight)
horizontal4.addWidget(checkbutton, alignment = Qt.AlignCenter)
answer = QLabel()
horizontal5.addWidget(answer, alignment = Qt.AlignCenter)


vertical.addLayout(horizontal1)
vertical.addLayout(horizontal2)
vertical.addLayout(horizontal3)
vertical.addLayout(horizontal4)
vertical.addLayout(horizontal5)

main_win.setLayout(vertical)

def check_answer():
    if group.checkedId() == 4:
        correct_answer = answer.setText('That is the correct answer!')
    else:
        correct_answer = answer.setText('That is incorrect, try again!')

checkbutton.clicked.connect(check_answer)

app.exec_()