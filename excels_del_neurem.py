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

    ctrl = hwp.HeadCtrl  # 문서 처음의 컨트롤(구역 정의) 선택
    while ctrl:  # 모든 컨트롤을 순회하면서
        if ctrl.UserDesc == "누름틀":  # 컨트롤 이름이 "누름틀"이면
            hwp.DeleteCtrl(ctrl)  # 해당 컨트롤(누름틀)을 삭제
        ctrl = ctrl.Next  # 다음 컨트롤 선택(다음 컨트롤이 없으면 None이 지정됨)   
             
    a.save("예산완료")
    hwp.Clear(1)
    hwp.Quit()



