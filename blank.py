import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *

def blank(left,right,top1,bottom,top2,bottom2):
    # 아래부터 페이지 여백 설정하는 코드
    hwp.HAction.GetDefault("PageSetup", hwp.HParameterSet.HSecDef.HSet)  # 초기화

    hwp.HParameterSet.HSecDef.PageDef.LeftMargin = hwp.MiliToHwpUnit(left)  # 좌측여백
    hwp.HParameterSet.HSecDef.PageDef.RightMargin = hwp.MiliToHwpUnit(right)  # 우측여백
    hwp.HParameterSet.HSecDef.PageDef.TopMargin = hwp.MiliToHwpUnit(top1)  # 상단여백
    hwp.HParameterSet.HSecDef.PageDef.BottomMargin = hwp.MiliToHwpUnit(bottom)  # 하단여백
    hwp.HParameterSet.HSecDef.PageDef.HeaderLen = hwp.MiliToHwpUnit(top2)  # 머릿말
    hwp.HParameterSet.HSecDef.PageDef.FooterLen = hwp.MiliToHwpUnit(bottom2)  # 꼬릿말
    hwp.HParameterSet.HSecDef.HSet.SetItem("ApplyClass", 24)  # 적용범위 분류
    hwp.HParameterSet.HSecDef.HSet.SetItem("ApplyTo", 3)  # 적용범위

    hwp.HAction.Execute("PageSetup", hwp.HParameterSet.HSecDef.HSet)  # 실행

if __name__=='__main__':
    a=mod_hwp()
    blank(20,20,15,15,10,10)
    
    a.save("여백")

    hwp.Clear(1)
    hwp.Quit()


