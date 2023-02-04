import win32com.client as win32

class contents():
    def __init__(self):
        self.hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
        self.hwp.XHwpWindows.Item(0).Visible=False
        self.hwp.RegisterModule("FilePathCheckDLL", "hwpCtrlModule")

    def open2(self,pos,name):
        position=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\{pos}\\{name}.hwpx"
        self.hwp.Open(position)
        self.title=name

    def get_text(self):
        self.hwp.InitScan(Range=0xff)
        self.total_text=''
        self.state=2
        while self.state not in [0,1]:
            self.state,self.text=self.hwp.GetText()
            self.total_text+=self.text
        return self.total_text
    def add_contents(self):
        self.hwp.FindCtrl()
        self.hwp.Run("ShapeObjTableSelCell")
        self.contents=[]
        self.contents.append(self.get_text())
        while self.hwp.HAction.Run("TableRightCell"):
            self.contents.append(self.get_text())
        return self.contents
    
    def get_contents(self,pos,name):
        self.open2(pos,name)    
        ctrl=self.hwp.HeadCtrl
        self.total_contents=[]
        while ctrl:
            if ctrl.CtrlID=="tbl":
                self.hwp.Run("MoveDown")
                self.hwp.SetPosBySet(ctrl.GetAnchorPos(0))
                self.total_contents.append(self.add_contents())
                ctrl=ctrl.Next
            else:
                ctrl=ctrl.Next
            # break
        title=self.title
        depart=self.total_contents[2][1]+self.total_contents[2][7]    
        per1=self.total_contents[2][4]    
        tel1=self.total_contents[2][5].replace("(","").replace(")","")
        per2=self.total_contents[2][10]
        rank=self.total_contents[2][9]
        tel2=self.total_contents[2][11].replace("(","").replace(")","")
        press=self.total_contents[1][1]         
        release=self.total_contents[1][3]        
        explain=self.total_contents[3]             
        self.hwp.Clear(1)
        return title,press,release,depart,per1,tel1,per2,rank,tel2,explain
    def quit(self):    
        self.hwp.Quit()

class excels():
    def __init__(self):
        self.excel=win32.gencache.EnsureDispatch("Excel.Application")
        self.excel.Visible=False

    def open(self,pos,name):
        position=f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\{pos}\\{name}.xlsx"
        self.wb= self.excel.Workbooks.Open(position)
        self.ws=self.wb.Worksheets(1)

    def save_value(self,value:list):
        for j in range(10):
            self.ws.Cells(i+2,j+1).Value=value[j]
            # self.ws.Cells(i+2,2).Value=value[1]
            # self.ws.Cells(i+2,3).Value=value[2]
            # self.ws.Cells(i+2,4).Value=value[3]
            # self.ws.Cells(i+2,5).Value=value[4]
            # self.ws.Cells(i+2,6).Value=value[5]
            # self.ws.Cells(i+2,7).Value=value[6]
            # self.ws.Cells(i+2,8).Value=value[7]
            # self.ws.Cells(i+2,9).Value=value[8]
            # self.ws.Cells(i+2,10).Value=value[9]

    def quit(self,pos,name):    
        self.wb.SaveAs(f"C:\\Users\\xkr04\\OneDrive\\바탕 화면\\코딩\\hwp\\{pos}\\{name}.xlsx")
        self.excel.Quit()

if __name__=='__main__':
    a=contents()
    b=excels()
    b.open("기재부","기재부 보도")
    for i in range(1,9):
        list=a.get_contents("기재부",f"기재부{i}")
        b.save_value(list)
    a.quit()
    b.quit("기재부","기재부3")

