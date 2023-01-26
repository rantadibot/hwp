from PySide6.QtWidgets import *

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("찾기")
        self.resize(600,40)

        self.layout = QVBoxLayout()
        vbox0 = QHBoxLayout()
        vbox1 =QVBoxLayout()
        vbox2 =QVBoxLayout()
        vbox3 =QVBoxLayout()
        vbox4 =QVBoxLayout()
        message = QLabel("찾을 내용: ")
        le=QLineEdit()

        vbox0.addWidget(message)
        vbox0.addWidget(le)

        a=QCheckBox("대/소문자 구분")
        b=QCheckBox("주위에 배치")
        vbox1.addWidget(a)
        vbox1.addWidget(b)

        c=QPushButton("다음 찾기")
        d=QPushButton("취소")
        c.clicked.connect(self.accept)
        d.clicked.connect(self.reject)

        message2 = QLabel("방향")
        e=QRadioButton('위로')
        f=QRadioButton('아래로')


        vbox2.addWidget(message2)
        vbox4.addWidget(e)
        vbox4.addWidget(f)
        # self.layout.addWidget(self.buttonBox)
        vbox3.addWidget(c)
        vbox3.addWidget(d)
        
        self.setLayout(vbox0)
        vbox0.addLayout(vbox3)
        # vbox0.addLayout(vbox1)
        # vbox2.addLayout(vbox4)
        # vbox1.addLayout(vbox2)
        # self.setLayout(vbox1)
        # self.setLayout(vbox2)
        # self.setLayout(vbox3)

app=QApplication()
a=CustomDialog()
a.show()
app.exec()  