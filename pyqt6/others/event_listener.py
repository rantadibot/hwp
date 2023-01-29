import sys
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication,QPushButton,QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("시작해")
        self.setWindowIcon(QIcon(r'C:\Users\user\Desktop\새 폴더\기재부\moef.jpg'))
        btn0=QPushButton(icon=QIcon(r'C:\Users\user\Desktop\새 폴더\기재부\moef.jpg'),text="클릭해",parent=self)
        btn0.clicked.connect(self.btn_is_clicked)
        btn0.released.connect(self.btn_is_released)
        self.setCentralWidget(btn0)
        # self.setCentralWidget(btn1)
        self.setFixedSize(QSize(500,400))
        
    def btn_is_clicked(self):
        print("clicked")    
    def btn_is_released(self):
        print("released")    
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()