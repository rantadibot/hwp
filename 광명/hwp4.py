from start import hwp
from tkinter import Tk
from time import sleep
import os

if __name__ == '__main__':
    # root = Tk()
    # filename = askopenfilename()
    # root.destroy()
    
    # a=mod_hwp()
    # a.open2(filename)
    # a.move()
    # page_num = hwp.PageCount  # 전체 페이지 수를 page_num에 저장
    # print(page_num)
        
    filepath=r'C:\Users\user\Desktop\새 폴더\기재부'
    hwp.XHwpDocuments.Add(isTab=True)  # 새 탭으로 빈 문서 열기
    hwp.SaveAs(os.path.join(filepath,"합체.hwpx"))
    
    for i in range(2):  # 페이지 수만큼 반복
        hwp.Open(os.path.join(filepath, str(i+1)+ ".hwpx"))
        hwp.Run("CopyPage")  # 현재쪽 복사
        hwp.Open(os.path.join(filepath,"합체.hwpx"))  # 새 탭으로 빈 문서 열기
        hwp.Run("PastePage")  # 새 탭에 붙여넣기
        hwp.Save()
        sleep(0.2)
    hwp.Run("MoveTopLevelBegin")  # 문서최상단으로 이동 == hwp.MovePos(2)
    hwp.Run("DeletePage")  # 현재쪽(빈 페이지) 삭제
    hwp.Save()
    hwp.XHwpDocuments.Item(0).Close(isDirty=False)  # 탭 닫기
    hwp.Quit()
