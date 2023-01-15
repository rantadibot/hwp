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


def getName(name):
    page_count = hwp.XHwpDocuments.Item(0).XHwpDocumentInfo.PageCount
    for i in range(page_count):
        if hwp.GetFieldText(f"담당자{{{{{i}}}}}") == name:
            return hwp.GetFieldText(f"프로그램{{{{{i}}}}}")

if __name__=='__main__':
    a=mod_hwp()
    a.open("예산완료2")
    print(getName("최대집"))
    hwp.Clear(1)
    hwp.Quit()
    excel.Quit()


