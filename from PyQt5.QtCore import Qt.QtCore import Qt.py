from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Жесть какая-то,.')
my_win.move(900, 70)
my_win.resize(400, 200)
my_win.show()
button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')
layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(button1, alignment = Qt.AlignLeft)
layoutH1.addWidget(button2, alignment = Qt.AlignRight)
layoutH2.addWidget(button3, alignment = Qt.AlignCenter)
layoutH3.addWidget(button4, alignment = Qt.AlignLeft)
layoutH3.addWidget(button5, alignment = Qt.AlignRight)
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)
window.setLayout(layoutV)
app.exec_()





