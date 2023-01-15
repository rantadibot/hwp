import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

excel=win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible=False

wb= excel.Workbooks.Open("C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\보도.xlsx")
ws=wb.Worksheets(1)

def putField(value):
    field_list=hwp.GetFieldList().split("\x02")
    print(field_list)
    for idx,field in enumerate(field_list):
        hwp.PutFieldText(f"{field}{{{{{0}}}}}",value[idx])
        
if __name__=='__main__':
    b=mod_hwp()
    b.open2("기재부","기재부3")
    data = list(ws.Range(ws.Cells(3,1),
                ws.Cells(3, 12)).Value[0])
    putField(data)
    print(data)
    b.save("기재부")        
    hwp.Clear(1)
    hwp.Quit()
    excel.Quit()



