import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")

class mod_hwp:
    def __init__(self):
        hwp.XHwpWindows.Item(0).Visible=True
        hwp.RegisterModule("FilePathCheckDLL", "hwpCtrlModule")

    def open(self,name):
        position=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\{name}.hwp"
        hwp.Open(position)

    def opens(self,name):
        position=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\{name}.hwpx"
        hwp.Open(position,arg="suspendpassword:True;versionworning:False")

    def open2(self,pos,name):
        position=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\{pos}\\{name}.hwpx"
        hwp.Open(position)

    def insert_text(self,text):
        hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.HParameterSet.HInsertText.Text = text
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

    def save(self,name):
        position=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\{name}.hwp"
        hwp.SaveAs(position)

    def getField(self):
        field_list=hwp.GetFieldList(1).split("\x02")
        for i in field_list:
            print(i,hwp.GetFieldText(i))
