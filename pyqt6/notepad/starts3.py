from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication,QDate,QTime,Qt
from PySide6.QtGui import QIcon
from finds3 import findWindow

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
        self.fontSize = 15
        self.setWindowIcon(QIcon(r'C:\Users\user\Desktop\새 폴더\기재부\a.png'))
        self.setWindowTitle("Windows 메모장")
        self.windows = []
        self.statusBar()
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint| Qt.WindowCloseButtonHint)

        self.opend=False
        self.opend_file_path='제목없음'
        self.dialog=QDialog()

        self.setGeometry(300, 300, 300, 200)
        self.resize(1200,600)
        wg = MyWidget()
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
                   
    def add_act(self,act_name,act_key,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.triggered.connect(act_fun)

    def add_act_short(self,act_name,act_key,act_short,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(act_short)
       self.act.triggered.connect(act_fun)
                     
    def add_act_ctrl(self,act_name,act_key,act_short,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+{act_short}')
       self.act.triggered.connect(act_fun)
                 
    def add_act_ctrl2(self,act_name,act_key,act_short,act_fun=None):
       self.act=self.add.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+{act_short}')
       self.act.triggered.connect(act_fun)
                    
    def add_act_shift(self,act_name,act_key,act_short,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+Shift+{act_short}')
       self.act.triggered.connect(act_fun)
       
    def add_sep(self):
        self.file_menu.addSeparator()

    def make_menu(self):
        self.add_menu('파일','F')
        self.add_act_ctrl('새로 만들기','N','N')
        self.add_act_shift('새 창','W','N',self.add_window)
        self.add_act_ctrl('열기','O','O',self.open_file)
        self.add_act_ctrl('저장','S','S',self.save_file)
        self.add_act_shift('다른 이름으로 저장','A','S',self.saveas_file)
        self.add_sep()
        self.add_act('페이지 설정','U')
        self.add_act_ctrl('인쇄','P','P')
        self.add_sep()
        self.add_act('끝내기','X',self.exit)
        
        self.add_menu('편집','U')
        self.add_act_ctrl('실행 취소','T','Z',self.undo)
        self.add_sep()
        self.add_act_ctrl('잘라내기','X','X',self.cut)
        self.add_act_ctrl('복사','C','C',self.copy)
        self.add_act_ctrl('붙여넣기','P','V',self.paste)
        self.add_act_short('삭제','L','Del',self.clear)
        self.add_sep()
        self.add_act_ctrl('Bing으로 검색','S','E')
        self.add_act_ctrl('찾기','T','F',findWindow.find)
        self.add_act_short('다음 찾기','F','F3')
        self.add_act_short('이전 찾기','N','Shift+F3')
        self.add_act_ctrl('바꾸기','R','H')
        self.add_act_ctrl('이동','G','G')
        self.add_sep()
        self.add_act_ctrl('모두 선택','A','A')
        self.add_act_short('시간/날짜','D','F5',self.getTime)
        
        self.add_menu('서식','O')
        self.add_act('자동 줄바꿈','W')
        self.add_act('글꼴','F')
        
        self.add_menu('보기','V')
        self.add_menu2('확대하기/ 축소하기','S')
        self.add_act_ctrl2('확대','I','+',self.fontSizeUp)
        self.add_act_ctrl2('축소','O','-',self.fontSizeDown)
        self.add_act_ctrl2('확대하기/ 축소하기 기본값 복원','O',0,self.fontSizeReturn)
        self.add_act('상태 표시줄','S')

        self.add_menu('도움말','H')
        self.add_act('도움말 보기','H')
        self.add_act('피드백 보내기','F')
        self.add_sep()
        self.add_act('메모장 정보','A')

    def save_changed_data(self):
       msgBox=QMessageBox()
       msgBox.setText(f"변경 내용을 {self.opend_file_path}에 저장하시겠습니까")
       msgBox.addButton('저장',QMessageBox.YesRole)#0
       msgBox.addButton('저장 안 함',QMessageBox.NoRole)#1
       msgBox.addButton('취소',QMessageBox.RejectRole)#2
       ret=msgBox.exec_()
       return ret

    def exit(self):
       ret=self.save_changed_data()
       if ret!=2:
            self.close()
       
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
              self.opend=True
              self.opend_file_path=file[0]
                
    def save(self,fname):
        text = self.texts.toPlainText()
        with open(fname,'w',encoding='UTF-8') as f:
            f.write(text)
    
    def save_file(self):    
        if self.opend:
            self.save(self.opend_file_path)
        else:
            file=QFileDialog.getSaveFileName(self)
            if file[0]:
                self.save(file[0])
              
    def saveas_file(self):
        file=QFileDialog.getSaveFileName(self)
        if file[0]:
           self.save(file[0])
              
    def clear(self) :
        self.texts.clear()
        
    def fontSizeUp(self) :
        self.fontSize = self.fontSize + 1
        self.texts.setFontPointSize(self.fontSize)

    def fontSizeDown(self) :
        self.fontSize = self.fontSize - 1
        self.texts.setFontPointSize(self.fontSize)
        
    def fontSizeReturn(self) :
        self.fontSize = 15
        self.texts.setFontPointSize(self.fontSize)
    
    def getTime(self) :
        date=QDate.currentDate()
        time=QTime.currentTime().toString('hh:mm ap')
        if time[-2:]=='pm':
            times='오후 '+time[:-2]+' '+date.toString(Qt.ISODate) 
            
        else:
            times='오전 '+time[:-2]+' '+date.toString(Qt.ISODate)     
        self.texts.append(times)

    def undo(self):
        self.texts.undo()    
    def cut(self):
        self.texts.cut()    
    def copy(self):
        self.texts.copy()    
    def paste(self):
        self.texts.paste()    


