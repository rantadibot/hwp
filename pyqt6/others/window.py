import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        
        button1 = QPushButton("확인")  
        button2 = QPushButton("취소")
        button3 = QPushButton("적용(A)")
        
        tabs = QTabWidget()
        tabs.addTab(tab1, '컴퓨터 이름')
        tabs.addTab(tab2, '하드웨어')
        tabs.addTab(tab3, '고급')
        tabs.addTab(tab4, '시스템 보호 원격')
        
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
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())