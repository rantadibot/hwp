import sys
from PySide6.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tab1 = QWidget()
        self.add_tab1()
        
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        button1 = QPushButton("확인")  
        button2 = QPushButton("취소")
        button3 = QPushButton("적용(A)")
        
        tabs = QTabWidget()
        tabs.addTab(self.tab1, '일반')
        tabs.addTab(self.tab2, '바로 가기')
        tabs.addTab(self.tab3, '호환성')
        tabs.addTab(self.tab4, '보안')
        tabs.addTab(self.tab5, '자세히')
        tabs.addTab(self.tab6, '이전 버전')
        
        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('시스템 속성')
        self.setGeometry(400, 400, 350, 200)
        self.resize(412,550)
        self.show()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())