from PySide6.QtWidgets import QApplication,QPushButton,QMainWindow
from PySide6.QtWidgets import QLabel,QLineEdit,QVBoxLayout,QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("시작해")
        self.label=QLabel()
        self.input=QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout=QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        container=QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app=QApplication()
window=MainWindow()
window.show()
app.exec()