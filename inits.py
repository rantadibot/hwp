import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

def putField(add1,add2,add3,add4):
    hwp.PutFieldText("23 예산",add1)
    hwp.PutFieldText("23 중기",add2)
    hwp.PutFieldText("24 요구",add3)
    hwp.PutFieldText("24 실무",add4)

# insert_text("저글링")
# save("a")

if __name__=='__main__':
    a=mod_hwp()
    a.open("예산")
    putField(100000,200000,300000,150000)
    a.save("연대")
    hwp.Clear(1)

    a.open("예산")
    putField(300000,120000,140000,1500000)
    a.save("고대")
    hwp.Quit()



