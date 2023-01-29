from PySide6.QtWidgets import *

class MyApps2(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def add_tab2(self):
        high_box=QVBoxLayout()

        hbox0 = QHBoxLayout()
        hbox0.addWidget(QLabel('한글 2018'))
    
        vbox1 = QGridLayout()
        vbox1.addWidget(QHLine(),0,0,1,2)
        vbox1.addWidget(QLabel('대상 형식 : '),1,0,1,1)
        vbox1.addWidget(QLabel('응용 프로그램'),1,1,1,1)
        vbox1.addWidget(QLabel('대상위치 : '),2,0,1,1)
        vbox1.addWidget(QLabel('Bin'),2,1,1,1)
        vbox1.addWidget(QLabel('대상(T) : '),3,0,1,1)
        line1=QLineEdit(r'"C:\Program Files (x86)\HNC\Office 2018\HOffice100\Bin\Hwp.exe"')
        line1.setMaximumSize(300,25)
        vbox1.addWidget(line1,3,1,1,1)
        vbox1.addWidget(QHLine(),4,0,1,2)
        
        vbox2 = QGridLayout()

        vbox2.addWidget(QLabel('시작 위치(S) : '),0,0,1,1)
        line2=QLineEdit(r'"C:\Program Files (x86)\HNC\Office 2018\HOffice100\Bin"')
        line2.setMaximumSize(300,25)
        vbox2.addWidget(line2,0,1,1,1)
        vbox2.addWidget(QLabel('바로 가기 키(K) : '),1,0,1,1)
        line3=QLineEdit('없음')
        line3.setMaximumSize(300,25)
        vbox2.addWidget(line3,1,1,1,1)
        vbox2.addWidget(QLabel('실행(R) : '),2,0,1,1)
        com0=QComboBox()
        com0.addItems(['기본 창','최소 창','최대 창'])
        vbox2.addWidget(com0,2,1,1,1)
        vbox2.addWidget(QLabel('설명(O) : '),3,0,1,1)
        line4=QLineEdit('다양하고 강력한 편집 기능으로 보다 신속하고 간편하게 문서를 만듭니다.')
        line4.setMaximumSize(300,25)
        vbox2.addWidget(line4,3,1,1,1)

        vbox3 = QGridLayout()
        btn0=QPushButton('파일 위치 열기(F)')
        btn1=QPushButton('아이콘 변경(C)')
        btn2=QPushButton('고급(D)')
        vbox3.addWidget(btn0,0,0,1,1)
        vbox3.addWidget(btn1,0,1,1,1)
        vbox3.addWidget(btn2,0,2,1,1)
        high_box.addLayout(hbox0)
        high_box.addLayout(vbox1)
        high_box.addLayout(vbox2)
        high_box.addLayout(vbox3)
        self.tab2.setLayout(high_box)

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
