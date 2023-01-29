from PySide6.QtWidgets import *

class MyApps(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def add_tab1(self):
        high_box=QGridLayout()

        high_box.addWidget(QLineEdit('한글 2018'),0,1,1,1)
        high_box.addWidget(QHLine(),1,0,1,3)
        high_box.addWidget(QLabel('파일 형식 : '),2,0,1,1)
        high_box.addWidget(QLabel('바로 가기(.lnk)'),2,1,1,1)
        high_box.addWidget(QLabel('설명 : '),3,0,1,1)
        high_box.addWidget(QLabel('HWP 2018'),3,1,1,1)
        high_box.addWidget(QHLine(),4,0,1,3)
        
        high_box.addWidget(QLabel('위치 : '),5,0,1,1)
        high_box.addWidget(QLabel(r'C:\Users\Public\Desktop'),5,1,1,1)
        high_box.addWidget(QLabel('크기 : '),6,0,1,1)
        high_box.addWidget(QLabel('1.37KB (1,413 바이트)'),6,1,1,1)
        high_box.addWidget(QLabel('디스크 할당 크기 : '),7,0,1,1)
        high_box.addWidget(QLabel('4.00KB (4,096 바이트)'),7,1,1,1)
        high_box.addWidget(QHLine(),8,0,1,3)

        high_box.addWidget(QLabel('만든 날짜'),9,0,1,1)
        high_box.addWidget(QLabel('2020년 2월 14일 금요일, 오후 11:11:28'),9,1,1,1)
        high_box.addWidget(QLabel('수정한 날짜'),10,0,1,1)
        high_box.addWidget(QLabel('2020년 2월 14일 금요일, 오후 11:11:28'),10,1,1,1)
        high_box.addWidget(QLabel('액세스한 날짜'),11,0,1,1)
        high_box.addWidget(QLabel('2023년 1월 29일 오늘, 14시간 전'),11,1,1,1)
        high_box.addWidget(QHLine(),12,0,1,3)

        high_box.addWidget(QLabel('특성 : '),13,0,1,1)
        chk0=QCheckBox('읽기 전용(R)')
        chk1=QCheckBox('숨김(H)')
        btn=QPushButton('고급(D)')
        high_box.addWidget(chk0,13,1,1,1)
        high_box.addWidget(chk1,13,2,1,1)
        high_box.addWidget(btn,13,3,1,1)

        self.tab1.setLayout(high_box)

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

