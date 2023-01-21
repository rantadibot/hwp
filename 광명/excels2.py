import win32com.client as win32
import tkinter as tk
from tkinter.filedialog import askopenfilename

def excels(filepath):
    excel = win32.gencache.EnsureDispatch("Excel.Application")
    excel.Visible = False
    wb = excel.Workbooks.Open(filepath)
    ws = wb.Worksheets(1)
    return excel,wb,ws

def dict(data):
    data = {i: j for (i, j) in data[1:]}
    return data

def hwps(filepath):
    hwp = win32.gencache.EnsureDispatch("hwpframe.hwpobject")
    hwp.RegisterModule("FilePathCheckDLL", "hwpCtrlModule")
    hwp.XHwpWindows.Item(0).Visible = True
    # hwp.Open(r'C:\Users\user\Desktop\새 폴더\기재부\오빠.hwp')
    hwp.Open(filepath)
    return hwp


# 자동교정 매크로를 파이썬 함수로 정의
def auto(target):
    hwp.HAction.GetDefault("AllReplace", hwp.HParameterSet.HFindReplace.HSet)
    hwp.HParameterSet.HFindReplace.Direction = hwp.FindDir("AllDoc")
    hwp.HParameterSet.HFindReplace.FindString = target
    hwp.HParameterSet.HFindReplace.ReplaceString = excel_data[target]
    hwp.HParameterSet.HFindReplace.ReplaceMode = 1
    hwp.HParameterSet.HFindReplace.IgnoreMessage = 1
    hwp.HParameterSet.HFindReplace.FindType = 1
    hwp.HAction.Execute("AllReplace", hwp.HParameterSet.HFindReplace.HSet)

def saves(name):
    hwp.SaveAs(rf'C:\Users\user\Desktop\새 폴더\기재부\{name}.hwpx')
    hwp.Clear(option=1)
    hwp.Quit()    

# 한/글 문서 자동교정 실행
def replace(data):
    for i in data.keys():
        auto(i)

if __name__ == '__main__':
    root = tk.Tk()  # GUI 실행하고
    root.withdraw()  # GUI 콘솔창 안나타나게
    excel_path = askopenfilename(title="교정표 엑셀 파일을 선택해주세요.",
                              initialdir=r'C:\Users\user\Desktop\새 폴더\기재부',
                              filetypes=[("엑셀파일", "*.xls *.xlsx *.cell")])

    hwp_path = askopenfilename(title="교정한 한/글 파일을 선택해주세요.",
                              initialdir=r'C:\Users\user\Desktop\새 폴더\기재부',
                              filetypes=[("아래아한글파일", "*.hwp *.hwpx")])
    root.destroy()  # GUI 종료

    excel, wb, ws = excels(excel_path)
    excel_data = dict(ws.UsedRange())
    excel.Quit()

    hwp = hwps(hwp_path)
    replace(excel_data)    
# hwp.SaveAs(r'C:\Users\user\Desktop\새 폴더\기재부\누나.hwpx')
    saves('마린')