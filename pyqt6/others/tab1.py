from PySide6.QtWidgets import *

class MyApps(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def add_tab1(self):
        high_box=QVBoxLayout()

        hbox0 = QHBoxLayout()
        a=QLineEdit()
        a.setPlaceholderText('한글 2018')
        hbox0.addWidget(a)
    
        vbox1 = QGridLayout()
        vbox1.addWidget(QLabel('파일 형식 : '),0,0,1,1)
        vbox1.addWidget(QLabel('바로 가기(.lnk)'),0,1,1,1)
        vbox1.addWidget(QLabel('설명 : '),1,0,1,1)
        vbox1.addWidget(QLabel('HWP 2018'),1,1,1,1)
        vbox1.addWidget(QHLine(),2,0,1,2)
        
        vbox2 = QGridLayout()

        vbox2.addWidget(QLabel('위치 : '),0,0,1,1)
        vbox2.addWidget(QLabel(r'C:\Users\Public\Desktop'),0,1,1,1)
        vbox2.addWidget(QLabel('크기 : '),1,0,1,1)
        vbox2.addWidget(QLabel('1.37KB (1,413 바이트)'),1,1,1,1)
        vbox2.addWidget(QLabel('디스크 할당 크기 : '),2,0,1,1)
        vbox2.addWidget(QLabel('4.00KB (4,096 바이트)'),2,1,1,1)
        vbox2.addWidget(QHLine(),3,0,1,2)

        vbox3 = QGridLayout()

        vbox3.addWidget(QLabel('만든 날짜'),0,0,1,1)
        vbox3.addWidget(QLabel('2020년 2월 14일 금요일'),0,1,1,1)
        vbox3.addWidget(QLabel('수정한 날짜'),1,0,1,1)
        vbox3.addWidget(QLabel('1.37KB (1,413 바이트)'),1,1,1,1)
        vbox3.addWidget(QLabel('액세스한 날짜'),2,0,1,1)
        vbox3.addWidget(QLabel('4.00KB (4,096 바이트)'),2,1,1,1)
        vbox3.addWidget(QHLine(),3,0,1,2)

        vbox4 = QGridLayout()
        vbox4.addWidget(QLabel('특성 : '),0,0,1,1)
        chk0=QCheckBox('읽기 전용(R)')
        chk1=QCheckBox('숨김(H)')
        btn=QPushButton('고급(D)')
        vbox4.addWidget(chk0,0,1,1,1)
        vbox4.addWidget(chk1,0,2,1,1)
        vbox4.addWidget(btn,0,3,1,1)
        high_box.addLayout(hbox0)
        high_box.addLayout(vbox1)
        high_box.addLayout(vbox2)
        high_box.addLayout(vbox3)
        high_box.addLayout(vbox4)

        self.tab1.setLayout(high_box)

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

