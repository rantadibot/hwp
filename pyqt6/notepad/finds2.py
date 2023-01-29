from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
class findWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint| Qt.WindowCloseButtonHint)
        self.setWindowTitle("찾기")
        # self.resize(600,40)
        vbox0 = QHBoxLayout()
        self.msg = QLabel("찾을 내용: ")
        self.le=QLineEdit()
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

        self.rad0=QRadioButton('위로')
        self.rad1=QRadioButton('아래로')

        vbox0.addWidget(self.msg)
        vbox0.addWidget(self.le)
        vbox0.addLayout(vbox1)
        vbox0.addLayout(vbox2)
        vbox0.addWidget(self.rad0)
        vbox0.addWidget(self.rad1)

        self.btn0.clicked.connect(self.find_word)
        self.btn1.clicked.connect(self.close)

        self.setLayout(vbox0)
        self.show()
  
    def find(self):
        a=findWindow()
        a.exec()

    def find_word(self):
        print(self.chk0.isChecked())
        print(self.le.text())
        
    def keyReleaseEvent(self,event):
        print(self.le.text())
        if self.le.text():
            self.btn0.setEnabled(True)
        else:
            self.btn0.setEnabled(False)
    