import win32com.client as win32

# 엑셀 실행
excel = win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible = False
wb = excel.Workbooks.Open(r'C:\Users\user\Desktop\새 폴더\기재부\교정3.xlsx')
ws = wb.Worksheets(1)

data = ws.UsedRange()[1:]
data = {i: j for (i, j) in data}
excel.Quit()

hwp = win32.gencache.EnsureDispatch("hwpframe.hwpobject")
hwp.RegisterModule("FilePathCheckDLL", "hwpCtrlModule")
hwp.XHwpWindows.Item(0).Visible = True
# hwp.Open(r'C:\Users\user\Desktop\새 폴더\기재부\오빠.hwp')
hwp.Open(r'C:\Users\user\Desktop\새 폴더\기재부\기재부3.hwpx')


# 자동교정 매크로를 파이썬 함수로 정의
def auto(target):
    hwp.HAction.GetDefault("AllReplace", hwp.HParameterSet.HFindReplace.HSet)
    hwp.HParameterSet.HFindReplace.Direction = hwp.FindDir("AllDoc")
    hwp.HParameterSet.HFindReplace.FindString = target
    hwp.HParameterSet.HFindReplace.ReplaceString = data[target]
    hwp.HParameterSet.HFindReplace.ReplaceMode = 1
    hwp.HParameterSet.HFindReplace.IgnoreMessage = 1
    hwp.HParameterSet.HFindReplace.FindType = 1
    hwp.HAction.Execute("AllReplace", hwp.HParameterSet.HFindReplace.HSet)


# 한/글 문서 자동교정 실행
for i in data.keys():
    auto(i)
    
# hwp.SaveAs(r'C:\Users\user\Desktop\새 폴더\기재부\누나.hwpx')
hwp.SaveAs(r'C:\Users\user\Desktop\새 폴더\기재부\주무관.hwpx')
hwp.Clear(option=1)
hwp.Quit()    