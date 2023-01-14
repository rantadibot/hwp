import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
hwp.RegisterModule("FilePathCheckDLL", "hwpCtrlModule")
hwp.XHwpWindows.Item(0).Visible = True
class mod_hwp:
    def __init__(self):
            self
            
    def open(self,name):
        hwp.Open(rf'C:\Users\user\Desktop\새 폴더\기재부\{name}.hwpx')
    def open2(self,name):
        hwp.Open(name)
    def save(self,name):
        hwp.SaveAs(rf'C:\Users\user\Desktop\새 폴더\기재부\{name}.hwpx')

        
    def getPage(self,num):
        print(hwp.GetPageText(num-1))
        
    def goto_page(self,num):
        hwp.HAction.GetDefault("Goto", hwp.HParameterSet.HGotoE.HSet)
        hwp.HParameterSet.HGotoE.SetSelectionIndex = 1
        hwp.HParameterSet.HGotoE.HSet.SetItem("DialogResult", num)
        hwp.HAction.Execute("Goto", hwp.HParameterSet.HGotoE.HSet)
            
    def move(self):
        hwp.MovePos(2) 
    