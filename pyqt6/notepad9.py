import sys
from starts3 import *

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=myapp()
    ex.make_menu()
    # ex.new_file()
    sys.exit(app.exec())