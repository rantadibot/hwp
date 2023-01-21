import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from start2 import mod_hwp,hwp
from charshapes import char,char2,char3

def start():
    hwp.Run("MoveDocBegin")
def end():
    hwp.Run("MoveDocEnd")
def height1():
    hwp.HAction.Run("CharShapeHeightIncrease")    
def height2():
    hwp.HAction.Run("CharShapeHeightDecrease")    
def height3():
    hwp.HAction.Run("ParagraphShapeIncreaseLineSpacing")    
def height4():
    hwp.Run("ParagraphShapeDecreaseLineSpacing")      
def select():
    hwp.Run("Select")      
def select_all():
    hwp.Run("SelectAll")      
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
    
    button1 = tk.Button(text="글씨 검은색", command=lambda:char('black'))
    button1.grid(column=0, row=1)
    button2 = tk.Button(text="글씨 빨간색", command=lambda:char('red'))
    button2.grid(column=1, row=1)
    button3 = tk.Button(text="글씨 청록색", command=lambda:char('bluish'))
    button3.grid(column=2, row=1)
    button3 = tk.Button(text="글씨 파란색", command=lambda:char('blue'))
    button3.grid(column=3, row=1)
    
    button4 = tk.Button(text="글씨 진하게", command=lambda:char2('bold'))
    button4.grid(column=0, row=2)
    button5 = tk.Button(text="글씨 이탤릭", command=lambda:char2('italic'))
    button5.grid(column=1, row=2)
    button5 = tk.Button(text="글씨 밑줄", command=lambda:char2('underline'))
    button5.grid(column=2, row=2)
    
    button6 = tk.Button(text="한글 종료", command=hwp_exit)
    button6.grid(column=0, row=3)
    
    button6 = tk.Button(text="글자크기 +", command=height1)
    button6.grid(column=0, row=4)
    button6 = tk.Button(text="글자크기 -", command=height2)
    button6.grid(column=1, row=4)
    button6 = tk.Button(text="줄간격 +", command=height3)
    button6.grid(column=2, row=4)
    button6 = tk.Button(text="줄간격 -", command=height4)
    button6.grid(column=3, row=4)
    
    button7 = tk.Button(text="새 줄", command=lambda:char3('line'))
    button7.grid(column=0, row=5)
    button7 = tk.Button(text="새페이지", command=lambda:char3('page'))
    button7.grid(column=1, row=5)
    button7 = tk.Button(text="새문단", command=lambda:char3('para'))
    button7.grid(column=2, row=5)
    
    button7 = tk.Button(text="단어선택", command=select)
    button7.grid(column=0, row=6)
    button7 = tk.Button(text="전체선택", command=select_all)
    button7.grid(column=1, row=6)
    win.mainloop()
