from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import *

class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Windows 메모장")
        self.windows = []
        self.statusBar()
        self.setGeometry(300, 300, 300, 200)
        self.resize(1200,600)
        self.show()

    def add_menu(self,name,key):       
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        #ALT+key, 이름은 name
        self.file_menu = menubar.addMenu(name)
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", f"{name}(&{key})", None))

        
    def add_menu2(self,name,key):       
        self.add=self.file_menu.addMenu(name)
        self.add.setTitle(QCoreApplication.translate("MainWindow", f"{name}(&{key})", None))
            
    def add_act(self,act_name,act_key):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       
    def add_act2(self,act_name,act_key,act_fun):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.triggered.connect(act_fun)

    def add_act_short(self,act_name,act_key,act_short):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(act_short)
              
    def add_act_ctrl(self,act_name,act_key,act_short):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+{act_short}')
       
    def add_act_ctrl2(self,act_name,act_key,act_short):
       self.act=self.add.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+{act_short}')
   
    def add_act_ctrl3(self,act_name,act_key,act_short,act_fun):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+{act_short}')
       self.act.triggered.connect(act_fun)
              
    def add_act_shift(self,act_name,act_key,act_short):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+Shift+{act_short}')
       
    def add_sep(self):
        self.file_menu.addSeparator()

    def exit(self):   
       self.act.triggered.connect(QApplication.quit)
       
    def open_file(self):
        file=QFileDialog.getOpenFileName(self)
        if file[0]:
           with open(file[0],encoding='UTF-8') as f:
              text=f.read()

    def save_file(self):
        file=QFileDialog.getSaveFileName(self)
        if file[0]:
           with open(file[0],'w',encoding='UTF-8') as f:
              f.write()
