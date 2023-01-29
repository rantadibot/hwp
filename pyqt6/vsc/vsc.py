import sys
from vsc_start import *

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=myapp()
    ex.make_menu()
    sys.exit(app.exec())