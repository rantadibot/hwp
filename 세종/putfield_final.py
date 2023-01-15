import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

excel=win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible=False

wb= excel.Workbooks.Open("C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\보도2.xlsx")
ws=wb.Worksheets(1)

def putField(value):
    field_list=hwp.GetFieldList().split("\x02")
    for idx,field in enumerate(field_list):
        hwp.PutFieldText(f"{field}{{{{{0}}}}}",value[idx])


if __name__=='__main__':
    b=mod_hwp()
    a=[2,3,4,5]
    for i in a:
        b.open2("기재부","산업부")
        data = list(ws.Range(ws.Cells(i,1),
                ws.Cells(i, 13)).Value[0])
        putField(data)
        print(data)
        b.save(f"산업부+{i}")
        hwp.Clear(1)

    hwp.Quit()
    excel.Quit()



