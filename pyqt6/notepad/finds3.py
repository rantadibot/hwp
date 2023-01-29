from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class findWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint| Qt.WindowCloseButtonHint)
        self.setWindowTitle("찾기")
        # self.resize(600,40)
        high_box = QGridLayout()
        vbox0=QHBoxLayout()
        self.msg = QLabel("찾을 내용: ")
        self.le=myTextEdit()
        
        vbox0.addWidget(self.msg)
        vbox0.addWidget(self.le)

        vbox1=QVBoxLayout()
        self.btn0=QPushButton('찾기')
        self.btn1=QPushButton('취소')

        vbox1.addWidget(self.btn0)
        vbox1.addWidget(self.btn1)
        
        vbox2=QVBoxLayout()
        self.chk0=QCheckBox('대/소문자 구분')
        self.chk1=QCheckBox('주위에 배치')
        vbox2.addWidget(self.chk0)
        vbox2.addWidget(self.chk1)

        vbox3=QHBoxLayout()
        self.rad0=QRadioButton('위로')
        self.rad1=QRadioButton('아래로')
        vbox3.addWidget(self.rad0)
        vbox3.addWidget(self.rad1)

        high_box.addLayout(vbox0,0,0,1,1)
        high_box.addLayout(vbox1,0,1,1,1)
        high_box.addLayout(vbox2,2,0,1,1)
        high_box.addLayout(vbox3,1,1,1,1)

        self.btn0.clicked.connect(self.find_word)
        self.btn1.clicked.connect(self.close)

        self.setLayout(high_box)
        self.show()
  
    def find(self):
        a=findWindow()
        a.exec()

    def find_word(self):
        print(self.chk0.isChecked())
        print(self.le.text())

class myTextEdit(QLineEdit):
     def __init__(self):
         QLineEdit.__init__(self)
         
     def keyReleaseEvent(self,e):
         print(self.text())
         if self.text():
             print('yes')
         else:
             print('no')
         
    