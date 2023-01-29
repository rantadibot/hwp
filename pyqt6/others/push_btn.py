import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication,QPushButton,QWidget

app=QApplication(sys.argv)
window=QWidget()
btn=QPushButton(icon=QIcon(r'C:\Users\user\Desktop\새 폴더\기재부\moef.jpg'),text="클릭해",parent=window)
window.show()
app.exec()