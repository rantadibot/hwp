import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from start import mod_hwp,hwp


def start():
    hwp.Run("MoveDocBegin")
def end():
    hwp.Run("MoveDocEnd")
def black():
    hwp.Run("CharShapeTextColorBlack")    
def red():
    hwp.Run("CharShapeTextColorRed")
def bluish():
    hwp.Run("CharShapeTextColorBluish")
def underline():
    hwp.HAction.Run("CharShapeUnderline")
def bold():
    hwp.HAction.Run("CharShapeBold")
def italic():
    hwp.HAction.Run("CharShapeItalic")
def height1():
    hwp.HAction.Run("CharShapeHeightIncrease")    
def height2():
    hwp.HAction.Run("CharShapeHeightDecrease")    
def replace():
    action = hwp.CreateAction("InsertText")  # action 변수 생성
    set = action.CreateSet()  # set 변수 생성(구조는 만들어지지만 값이 비어있음)
    action.GetDefault(set)  # set 초기화(현재 상태값으로 채움)
    set.SetItem("Text", "기획재정부")  # set 중 원하는 값 수정
    action.Execute(set)  # set 넣고 action 실행    
def hwp_exit():
    hwp.XHwpDocuments.Item(0).Close(isDirty=False)  # 탭 닫기
    hwp.Quit()
        
if __name__ == '__main__':
    root = Tk()
    filename = askopenfilename()
    root.destroy()
    
    a=mod_hwp()
    a.open2(filename)
    
    win = tk.Tk()

    button0 = tk.Button(text="문서 시작으로", command=start)
    button0.grid(column=0, row=0)
    button1 = tk.Button(text="문서 끝으로", command=end)
    button1.grid(column=1, row=0)
    button1 = tk.Button(text="글씨 검은색", command=black)
    button1.grid(column=0, row=1)
    button2 = tk.Button(text="글씨 빨간색", command=red)
    button2.grid(column=1, row=1)
    button3 = tk.Button(text="글씨 청록색", command=bluish)
    button3.grid(column=2, row=1)
    button4 = tk.Button(text="글씨 진하게", command=bold)
    button4.grid(column=0, row=2)
    button5 = tk.Button(text="글씨 이탤릭", command=italic)
    button5.grid(column=1, row=2)
    button5 = tk.Button(text="글씨 밑줄", command=underline)
    button5.grid(column=2, row=2)
    button6 = tk.Button(text="한글 종료", command=hwp_exit)
    button6.grid(column=0, row=3)
    button6 = tk.Button(text="글자크기 +", command=height1)
    button6.grid(column=0, row=4)
    button7 = tk.Button(text="글자크기 -", command=height2)
    button7.grid(column=1, row=4)
    button8 = tk.Button(text="기재부 추가", command=replace)
    button8.grid(column=2, row=4)
    win.mainloop()
