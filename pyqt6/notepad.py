import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QAction,QIcon

class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows 메모장")
        self.initUI()
    
    def initUI(self):
        exitAction = QAction('Exit', None)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&파일')
        
        # paste_menu = menubar.addMenu('&편집')
        # letter_menu = menubar.addMenu('&서식')
        # show_menu = menubar.addMenu('&보기')
        # help_menu = menubar.addMenu('&도움말')
        file_menu.addAction(exitAction)
        # file_menu.addAction('새창')
        # file_menu.addAction('새로만들기')

        self.setGeometry(300, 300, 300, 200)
        self.show()     

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=myapp()
    sys.exit(app.exec())