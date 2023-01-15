import win32com.client as win32
from pathlib import Path
from time import sleep
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
hwp.XHwpWindows.Item(0).Visible=True
hwp.RegisterModule("FilePathCheckDLL", "hwpCtrlModule")
path=Path(r'C:\Users\user\Desktop\새 폴더\기재부')
for file in path.glob("*.hwpx"):
    hwp.Open(file.absolute())
    print(hwp.GetPageText(0))
    sleep(1)
hwp.Quit()    