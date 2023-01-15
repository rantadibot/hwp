import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

if __name__=='__main__':
    a=mod_hwp()
    # hwp.HAction.GetDefault("InsertText",hwp.HParameterSet.HInsertText.HSet)
    # hwp.HParameterSet.HInsertText.Text = "야야야\r\n"
    # hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)

    act2 = hwp.CreateAction("InsertText")  # ParagraphShape(문단모양) 액션 생성
    pset2 = act2.CreateSet()  # 해당하는 파라미터셋 생성
    act2.GetDefault(pset2)  # 현재값 입력
    pset2.SetItem("Text","저글링")  # 줄간격 조회
    act2.Execute(pset2)

    a.save("야야")

    act = hwp.CreateAction("ParagraphShape")  # ParagraphShape(문단모양) 액션 생성
    pset = act.CreateSet()  # 해당하는 파라미터셋 생성
    act.GetDefault(pset)  # 현재값 입력
    print(pset.Item("LineSpacing"))  # 줄간격 조회

    hwp.Clear(1)
    hwp.Quit()


