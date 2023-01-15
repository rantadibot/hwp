import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

excel=win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible=False

wb= excel.Workbooks.Open("C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\예산.xlsx")
ws=wb.Worksheets(1)


def putField(index,value):
    field_list=["프로그램","담당자","23 예산","23 중기","24 요구","24 실무"]
    for idx,field in enumerate(field_list):
        hwp.PutFieldText(f"{field}{{{{{index}}}}}",value[idx])

if __name__=='__main__':
    a=mod_hwp()
    a.open("예산3")
    hwp.Run("CopyPage")
    row=2
    while True:
        if not ws.Cells(row,1).Value:
            hwp.Run("DeletePage")
            break
        else:
            data = list(
            ws.Range(ws.Cells(row,1),
                     ws.Cells(row, 6)).Value[0])
            putField(row-2,data)
            hwp.Run("PastePage")
            row+=1
   
    a.save("예산완료2")
    hwp.Clear(1)
    hwp.Quit()
    excel.Quit()



