from PySide6.QtWidgets import *

class MyApps6(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def add_tab6(self):
        high_box=QVBoxLayout()

        hbox0 = QHBoxLayout()
        lab0=QLabel('이전 버전은 파일 히스토리 또는 복원지점에서 가져옵니다')
        lab0.setMaximumWidth(300)
        hbox0.addWidget(lab0)

        vbox1 = QGridLayout()
        vbox1.addWidget(QLabel('파일 버전(F) : '),1,0,1,1)
        
        vbox3 = QGridLayout()
        btn0=QPushButton('열기(O)')
        btn1=QPushButton('복원(R)')
        vbox3.addWidget(btn0,0,0,1,1)
        vbox3.addWidget(btn1,0,1,1,1)
        high_box.addLayout(hbox0)
        high_box.addLayout(vbox1)
        high_box.addLayout(vbox3)
        self.tab6.setLayout(high_box)

