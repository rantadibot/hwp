import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

if __name__=='__main__':
    a=mod_hwp()
    a.open2("기재부","산업부1")
    print(hwp.GetFieldList().split("\x02"))
    hwp.Clear(1)
    a.open2("기재부","기재부2")
    print(a.getField())
    hwp.Clear(1)
    hwp.Quit()



