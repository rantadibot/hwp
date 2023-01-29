from PySide6.QtWidgets import QApplication,QPushButton,QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("시작해")
        self.btn=QPushButton(parent=self)
        self.setCentralWidget(self.btn)
        self.btn.setCheckable(True)
        self.btn.clicked.connect(self.btn_clicked)
        self.click_count=0
        
    def btn_clicked(self):
        self.click_count+=1
        self.btn.setText(f"{self.click_count}번 클릭함")  
app=QApplication()
window=MainWindow()
window.show()
app.exec()