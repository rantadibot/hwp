from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()    
        self.le = QTextEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 300)
        self.show()
                   
class myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fontSize = 10
        self.setWindowTitle("Windows 메모장")
        self.windows = []
        self.statusBar()
        self.setGeometry(300, 300, 300, 200)
        self.resize(1200,600)
        wg = MyWidget()
        # wg = MyWidget2()   # placeholder -- QWidget 상속하여 만든것으로 추후 교체하면 됨.
        self.setCentralWidget(wg)
        self.texts=wg.le
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

    def add_act_short2(self,act_name,act_key,act_short,act_fun):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(act_short)
       self.act.triggered.connect(act_fun)
                     
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
       
    def add_act_ctrl4(self,act_name,act_key,act_short,act_fun):
       self.act=self.add.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+{act_short}')
       self.act.triggered.connect(act_fun)
              
    def add_act_shift(self,act_name,act_key,act_short):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+Shift+{act_short}')
       
    def add_act_shift2(self,act_name,act_key,act_short,act_fun):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+Shift+{act_short}')
       self.act.triggered.connect(act_fun)
       
    def add_sep(self):
        self.file_menu.addSeparator()

    def exit(self):   
       self.act.triggered.connect(QApplication.quit)
       
    def add_window(self):  # 새 창(W)
        add_window = myapp()
        add_window.make_menu()
        self.windows.append(add_window)
        add_window.show()
           
    def open_file(self):
        file=QFileDialog.getOpenFileName(self)
        if file[0]:
           with open(file[0],encoding='UTF-8') as f:
              text=f.read()
              self.texts.setPlainText(text)

    def save_file(self):
        file=QFileDialog.getSaveFileName(self)
        if file[0]:
           text = self.texts.toPlainText()
           with open(file[0],'w',encoding='UTF-8') as f:
              f.write(text)

    def make_menu(self):
        self.add_menu('파일','F')
        self.add_act_ctrl('새로 만들기','N','N')
        self.add_act_shift2('새 창','W','N',self.add_window)
        self.add_act_ctrl3('열기','O','O',self.open_file)
        self.add_act_ctrl3('저장','S','S',self.save_file)
        self.add_act_shift('다른 이름으로 저장','A','S')
        self.add_sep()
        self.add_act('페이지 설정','U')
        self.add_act_ctrl('인쇄','P','P')
        self.add_sep()
        self.add_act2('끝내기','X',exit)
        
        self.add_menu('편집','U')
        self.add_act_ctrl('실행 취소','T','Z')
        self.add_sep()
        self.add_act_ctrl('잘라내기','X','X')
        self.add_act_ctrl('복사','C','C')
        self.add_act_ctrl('붙여넣기','P','V')
        self.add_act_short2('삭제','L','Del',self.clear)
        self.add_sep()
        self.add_act_ctrl('Bing으로 검색','S','E')
        self.add_act_ctrl('찾기','T','F')
        self.add_act_short('다음 찾기','F','F3')
        self.add_act_short('이전 찾기','N','Shift+F3')
        self.add_act_ctrl('바꾸기','R','H')
        self.add_act_ctrl('이동','G','G')
        self.add_sep()
        self.add_act_ctrl('모두 선택','A','A')
        self.add_act_short('시간/날짜','D','F5')
        
        self.add_menu('서식','O')
        self.add_act('자동 줄바꿈','W')
        self.add_act('글꼴','F')
        
        self.add_menu('보기','V')
        self.add_menu2('확대하기/ 축소하기','S')
        self.add_act_ctrl4('확대','I','+',self.fontSizeUp)
        self.add_act_ctrl4('축소','O','-',self.fontSizeDown)
        self.add_act_ctrl2('확대하기/ 축소하기 기본값 복원','O',0)
        self.add_act('상태 표시줄','S')

        self.add_menu('도움말','H')
        self.add_act('도움말 보기','H')
        self.add_act('피드백 보내기','F')
        self.add_sep()
        self.add_act('메모장 정보','A')

    def clear(self) :
        self.texts.clear()
        
    def fontSizeUp(self) :
        self.fontSize = self.fontSize + 1
        self.texts.setFontPointSize(self.fontSize)

    def fontSizeDown(self) :
        self.fontSize = self.fontSize - 1
        self.texts.setFontPointSize(self.fontSize)