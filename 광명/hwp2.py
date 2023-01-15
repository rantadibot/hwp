from start import mod_hwp,hwp
from tkinter import Tk
from tkinter.filedialog import askopenfilename

if __name__ == '__main__':
    root = Tk()
    filename = askopenfilename()
    root.destroy()
    
    a=mod_hwp()
    a.open2(filename)
    # a.getPage(2)
    a.goto_page(2)
    # a.move()
    a.save('기재부3.9')
    print(hwp.PageCount)
    hwp.Clear(option=1)
    hwp.Quit()