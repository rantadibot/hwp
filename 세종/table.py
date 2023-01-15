import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

if __name__=='__main__':
    a=mod_hwp()
    # hwp.HAction.GetDefault("InsertText",hwp.HParameterSet.HInsertText.HSet)
    # hwp.HParameterSet.HInsertText.Text = "야야야\r\n"
    # hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

    def insert(text):
        act2 = hwp.CreateAction("InsertText")  # ParagraphShape(문단모양) 액션 생성
        pset2 = act2.CreateSet()  # 해당하는 파라미터셋 생성
        act2.GetDefault(pset2)  
        pset2.SetItem("Text",text)  # 들어갈 단어 입력
        act2.Execute(pset2)

    def table(cols,rows,colwidth,rowheight):
        act = hwp.CreateAction("TableCreate")  # ParagraphShape(문단모양) 액션 생성
        pset = act.CreateSet()  # 해당하는 파라미터셋 생성
        act.GetDefault(pset)  
        pset.SetItem("Cols",cols)# 열 세 개
        pset.SetItem("Rows",rows)# 행 다섯 개
        pset.SetItem("WidthType", 2)  # 너비에 임의의 값 입력예정이라고 알려줌
        pset.SetItem("HeightType", 1)  # 높이에 임의의 값 입력예정이라고 알려줌

        pset_item = pset.CreateItemSet("TableProperties", "Table")  # 초기표속성 변경을 위한 아이템셋 생성
        pset_item.SetItem("TreatAsChar", True)  # 글자처럼 취급
        pset_col = pset.CreateItemArray("ColWidth", cols)  # 각 행의 높이를 정의하기 위한 배열 생성

        for i in range(cols):
            pset_col.SetItem(i, hwp.MiliToHwpUnit(colwidth))  # 열 너비 == colwidth  

        pset_row = pset.CreateItemArray("RowHeight", rows)  # 각 행의 높이를 정의하기 위한 배열 생성
        for j in range(rows):
            pset_row.SetItem(j, hwp.MiliToHwpUnit(rowheight))  # 행 높이 == rowheight
        act.Execute(pset)
    table(4,7,33.6,20)

    def next(text):
        insert(text)
        hwp.Run("TableRightCell")

    next("프로그램")
    next("23예산")
    next("23중기")
    next("24예산")
    # insert("프로그램")
    # hwp.Run("TableRightCell")
    # insert("23예산")
    # hwp.Run("TableRightCell")
    # insert("23중기")
    # hwp.Run("TableRightCell")
    # insert("24예산")
    # hwp.Run("TableRightCell")
    
    a.save("표4")

    hwp.Clear(1)
    hwp.Quit()


