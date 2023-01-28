import sys
from PySide6.QtWidgets import *
from tab1 import MyApps
from tab2 import MyApps2
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tab1 = QWidget()
        MyApps.add_tab1(self)
        
        self.tab2 = QWidget()
        MyApps2.add_tab2(self)

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




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())