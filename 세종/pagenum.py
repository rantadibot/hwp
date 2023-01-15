import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

def GetTableCellAddr():
    return hwp.KeyIndicator()[-1][1:].split(")")[0]

if __name__=='__main__':
    a=mod_hwp()
    a.open("표4")
    print(GetTableCellAddr())
    hwp.Clear(1)
    hwp.Quit()


