import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

if __name__=='__main__':
    a=mod_hwp()
    a.open("연예인")
    b=hwp.GetFieldList().split("\x02")

    print(b)
    for i in range(1,9):
        images=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\js\\book4\\image\\iu{i}.jpg"
        hwp.MoveToField(f"아이유{i}")
        hwp.InsertPicture(images, sizeoption=2)
    images2=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\js\\book4\\image\\김다미.jpg"
    hwp.MoveToField("김다미1")
    hwp.InsertPicture(images2, sizeoption=2)  
    a.save("연예인 사진")
    hwp.Clear(1)
    hwp.Quit()


