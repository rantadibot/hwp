import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start2 import *
import datetime as dt

def get():
    text = get_value()
    if text.endswith(""):
        hwp.Run('MoveNextPos')

def get_value():
    hwp.InitScan(Range=0xff)  # 추출범위를 선택영역으로 지정
    text = hwp.GetText()[1]  # 선택범위 문자열값 추출
    hwp.ReleaseScan()  # 검색종료
    return text

def get_weekday(text):
    week_list = ["월", "화", "수", "목", "금", "토", "일"]
    month, day = [int(i) for i in text.split(".")[:2]]
    week_num = dt.date(2023, month, day).weekday()
    week_day = week_list[week_num]
    return f"({week_day})"

def insert_text(text):
    act = hwp.CreateAction("InsertText")
    pset = act.CreateSet()
    pset.SetItem("Text", text)
    act.Execute(pset)

def get_end_addr():
    """
    표 안에서 마지막 셀까지 직접 다녀와보고
    제일 마지막 셀의 주소를 리턴하는 함수
    """
    hwp.HAction.Run("TableColEnd")
    hwp.HAction.Run("TableColPageDown")
    end_addr = hwp.KeyIndicator()[-1]
    hwp.HAction.Run("TableColBegin")
    hwp.HAction.Run("TableColPageUp")
    return end_addr


def cell_select():
    """
    셀 선택 상태가 아니면 선택해주는 함수
    """
    if hwp.SelectionMode != 3:
        hwp.Run("TableCellBlock")

def main():
    """
    실행방법: 표의 "A1" 셀에 커서를 두고 main 실행
    """
    cell_select()  # 먼저 셀 선택상태로 해 놓고
    end_addr = get_end_addr()  # 끝 셀의 주소를 저장해놓은 다음
    while True:  # 계속해서
        text = get_value()  # 해당 셀의 문자열이
        if text.endswith("."):  # "."으로 끝나면
            hwp.Run("Cancel")  # 셀 선택 취소
            hwp.Run("MoveLineEnd")  # 커서를 문자열 끝으로 옮겨놓고
            weekday = get_weekday(text)  # 해당 일자의 요일을 추출해서
            insert_text(weekday)  # 셀에 붙여넣는다.
            hwp.Run("TableCellBlock")  # 다시 셀 선택상태로
        if hwp.KeyIndicator()[-1] == end_addr:  # 끝 셀에 다다르면
            hwp.Run("Cancel")  # 선택상태 해제하고
            break  # while문 탈출
        hwp.Run("TableRightCell")  # 요일 붙여넣기 후 계속해서 한 셀씩 우측으로 이동


if __name__=='__main__':
    a=mod_hwp()
    a.opens("일정")

    while True:
        get()
        if hwp.KeyIndicator()[-1][1:3]=="A1":
            break
    main()
    hwp.Run("MovePageUp")
    while True:
        get()
        if hwp.KeyIndicator()[-1][1:3]=="A1":
            break
    main()
    hwp.Run("MoveDocBegin")
    a.save("일정4")
    hwp.Clear(1)
    hwp.Quit()


