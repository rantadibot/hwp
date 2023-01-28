from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication,QDate,QTime,Qt
from PySide6.QtGui import QIcon

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
        self.setWindowTitle("visual studio code")
        self.windows = []
        self.statusBar()
        
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

    def add_submenu(self,name):       
        self.add=self.file_menu.addMenu(name)
                   
    def add_act(self,act_name,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.triggered.connect(act_fun)

    def add_act_short(self,act_name,act_short,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setShortcut(act_short)
       self.act.triggered.connect(act_fun)
                     
    def add_act_ctrl(self,act_name,act_short,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setShortcut(f'Ctrl+{act_short}')
       self.act.triggered.connect(act_fun)
                 
    def add_act_ctrl2(self,act_name,act_short,act_fun=None):
       self.act=self.add.addAction(act_name)
       self.act.setShortcut(f'Ctrl+{act_short}')
       self.act.triggered.connect(act_fun)
                    
    def add_act_shift(self,act_name,act_key,act_short,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setText(QCoreApplication.translate("MainWindow", f"{act_name}(&{act_key})", None))
       self.act.setShortcut(f'Ctrl+Shift+{act_short}')
       self.act.triggered.connect(act_fun)

    def add_act_shift2(self,act_name,act_short,act_fun=None):
       self.act=self.file_menu.addAction(act_name)
       self.act.setShortcut(f'Ctrl+Shift+{act_short}')
       self.act.triggered.connect(act_fun)
       
    def add_sep(self):
        self.file_menu.addSeparator()

    def make_menu(self):
        self.add_menu('파일','F')
        self.add_act_ctrl('새 텍스트 파일','N')
        self.add_act('새 파일')
        self.add_act_shift2('새 창','N')
        self.add_sep()

        self.add_act_ctrl('파일 열기','O',self.open_file)
        self.add_act_ctrl('폴더 열기','S',self.save_file)
        self.add_act('파일 영역에서 작업영역 열기')
        self.add_submenu('최근 항목 열기') 
        self.add_sep()

        self.add_act('작업영역에 폴더 추가')
        self.add_sep()

        self.add_act_ctrl('저장','S',self.save_file)
        self.add_act_shift2('다른 이름으로 저장','S')
        self.add_act_ctrl('모두저장','K S',self.save_file)
        self.add_sep()

        self.add_submenu('공유') 
        self.add_sep()

        self.add_act('자동저장')
        self.add_submenu('기본 설정') 
        self.add_sep()

        self.add_act('파일 되돌리기')
        self.add_act_ctrl('편집기 닫기','F4',self.save_file)
        self.add_act_ctrl('폴더닫기','K F')
        self.add_act_ctrl('창닫기','K S',self.save_file)
        self.add_sep()

        self.add_act('끝내기',self.exit)
        
        self.add_menu('편집','E')
        self.add_act_ctrl('실행 취소','Z',self.undo)
        self.add_act_ctrl('다시 실행','Y',self.undo)
        self.add_sep()
        self.add_act_ctrl('잘라내기','X',self.cut)
        self.add_act_ctrl('복사','C',self.copy)
        self.add_act_ctrl('붙여넣기','P',self.paste)
        self.add_sep()

        self.add_act_ctrl('찾기','F',self.find)
        self.add_act_ctrl('바꾸기','H')
        self.add_sep()

        self.add_act_shift2('파일에서 찾기','F')
        self.add_act_shift2('파일에서 바꾸기','H')
        self.add_sep()

        self.add_act_ctrl('줄 주석 설정/해제','/')
        self.add_act_ctrl('블록 주석 설정/해제','G')
        self.add_act_short('Emmet : 약어 확장','Tab')
        
        self.add_menu('선택 영역','S')
        self.add_act('자동 줄바꿈')
        self.add_act('글꼴')
        
        self.add_menu('보기','V')
        self.add_act_shift2('명령 팔레트','P')
        self.add_act('뷰 열기')
        self.add_sep()

        self.add_submenu('모양')
        self.add_submenu('편집기 레이아웃')
        self.add_sep()

        self.add_act_shift2('탐색기','E')
        self.add_act_shift2('검색','F')
        self.add_act_shift2('소스제어','G')

        self.add_act('상태 표시줄')

        self.add_menu('이동','G')
        self.add_act('도움말 보기')
        self.add_act('피드백 보내기')
        self.add_sep()
        self.add_act('메모장 정보')

        self.add_menu('실행','R')
        self.add_act('도움말 보기')
        self.add_act('피드백 보내기')
        self.add_sep()
        self.add_act('메모장 정보')

        self.add_menu('터미널','T')
        self.add_act('도움말 보기')
        self.add_act('피드백 보내기')
        self.add_sep()
        self.add_act('메모장 정보')

        self.add_menu('도움말','H')
        self.add_act('도움말 보기')
        self.add_act('피드백 보내기')
        self.add_sep()
        self.add_act('메모장 정보')

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

    def find(self):
        self.le = QTextEdit()
        self.dialog.setWindowTitle("찾기")
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(300,200)
        btn_ok=QPushButton("찾기",self.dialog)
        btn_no=QPushButton("취소",self.dialog)
        btn_no.clicked.connect(self.dialog.close)
        self.dialog
        self.dialog.show()

