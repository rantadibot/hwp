import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start3 import *

if __name__=='__main__':
    a=mod_hwp()
    a.open2("기재부","기재부1")

    def get_text():
        hwp.InitScan(Range=0xff)
        total_text=''
        state=2
        while state not in [0,1]:
            state,text=hwp.GetText()
            total_text+=text
        return total_text
    def add_contents():
        hwp.FindCtrl()
        hwp.Run("ShapeObjTableSelCell")
        contents=[]
        contents.append(get_text())
        while hwp.HAction.Run("TableRightCell"):
            contents.append(get_text())
        return contents
    def get_contents():    
        ctrl=hwp.HeadCtrl
        total_contents=[]
        while ctrl:
            if ctrl.CtrlID=="tbl":
                hwp.Run("MoveDown")
                hwp.SetPosBySet(ctrl.GetAnchorPos(0))
                total_contents.append(add_contents())
                ctrl=ctrl.Next
            else:
                ctrl=ctrl.Next
            # break
        print(total_contents[1][1])         
        print(total_contents[1][3])         
        print(total_contents[3])         
        hwp.Clear(1)
        hwp.Quit()    


