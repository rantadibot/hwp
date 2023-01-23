import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from PySide6.QtCore import QObject, Signal, QEvent

def mySignal(widget):
    class Filter(QObject):
        clicked = Signal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True 	
            return False
    
    filter=Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked
	
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter any words')
        self.btn = QPushButton('save')
        self.btn.clicked.connect(self.updateTb)
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.checkBox1 = QCheckBox('Under line',self)
        self.checkBox2 = QCheckBox('Italic',self)
        self.checkBox1.toggled.connect(self.Bold)
        self.checkBox2.toggled.connect(self.Italic)
        self.col = QColor(0x00, 0x00, 0x00)
        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % self.col.name())
        self.frm.setGeometry(0, 0, 10, 10) 
        mySignal(self.frm).connect(self.showDialog)
        
        self.groupBoxLayout = QVBoxLayout() # Vertical layout 생성
        self.groupBoxLayout.addWidget(self.checkBox1)
        self.groupBoxLayout.addWidget(self.checkBox2)
        self.groupBoxLayout.addWidget(self.frm)
        self.grid = QGridLayout()
        self.grid.addWidget(self.le, 0, 0, 1, 3)
        self.grid.addWidget(self.btn, 0, 3, 1, 1)
        self.grid.addWidget(self.tb, 1, 0, 1, 3)
        self.grid.addLayout(self.groupBoxLayout, 1, 3, 1, 3)
        self.setLayout(self.grid)
        self.setWindowTitle('History')
        self.setGeometry(100, 100, 350, 150)
        self.show()
    
    def updateTb(self):
        self.tb.append(self.le.text())
    def Bold(self):
        self.tb.setFontUnderline(True) 
    def Italic(self):
        self.tb.setFontItalic(True)
    def showDialog(self):
        col = QColorDialog.getColor() 
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.tb.setTextColor(col) 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWidget()
	sys.exit(app.exec_())