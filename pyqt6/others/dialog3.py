import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(okButton)
        vbox.addWidget(cancelButton)
        vbox.addStretch(7)

        hbox = QHBoxLayout()
        hbox.addStretch(5)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())