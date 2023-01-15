import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *


if __name__=='__main__':
    a=mod_hwp()

    act=hwp.CreateAction("PageHiding")
    set=act.CreateSet()
    set.SetItem("Fields",32)
    act.Execute(set)

    # 값 확인
    act.GetDefault(set)
    print(set.Item("Fields"))

    a.save("실험")

    hwp.Clear(1)
    hwp.Quit()


