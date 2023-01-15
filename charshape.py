import win32com.client as win32
hwp=win32.gencache.EnsureDispatch("hwpframe.hwpobject")
from start3 import *
from time import sleep

def find_word(word, direction="Forward"):
    hwp.HAction.GetDefault("RepeatFind", hwp.HParameterSet.HFindReplace.HSet)
    hwp.HParameterSet.HFindReplace.Direction = hwp.FindDir(direction)
    hwp.HParameterSet.HFindReplace.FindString = word
    hwp.HParameterSet.HFindReplace.IgnoreMessage = 1
    hwp.HParameterSet.HFindReplace.FindType = 1
    status = hwp.HAction.Execute("RepeatFind", hwp.HParameterSet.HFindReplace.HSet)
    return


def select_sentence(target, end):
    """
    특정 단어를 포함한 문장 전체를 선택하는 함수. 문장구분은 "."가 기본값임.
    :param target: 검색할 문자열
    :type target: str
    :param end: 문장 구분 단위. 기본은 온점 "."
    :type end: str
    :return: start_pos 튜플
    :rtype: tuple
    """
    find_word(target, "Forward")
    find_word(end, "Backward")
    hwp.Run("MoveRight")
    start_pos = hwp.GetPos()
    find_word(end, "Forward")
    end_pos = hwp.GetPos()
    hwp.Run("Cancel")
    hwp.SetPos(*start_pos)
    hwp.Run("Select")
    hwp.SetPos(*end_pos)
    return start_pos


def change(color, bold=True):
    """
    선택한 구간의 속성을 변경하는 함수.
    :param color: 글자색
    :type color: str
    :param bold: 진하게할지말지
    :type bold: bool
    :return: None
    :rtype: None
    """
    if bold:
        hwp.Run("CharShapeBold")
    hwp.Run(f"CharShapeTextColor{color}")
    hwp.Run("Cancel")
    return

if __name__=='__main__':
    a=mod_hwp()
    a.open("대통령")
    hwp.MovePos(2)
    pos_set = set()
    while True:
        pos = select_sentence("국무회의", ".")
        if pos not in pos_set:
            sleep(1)
            pos_set.add(pos)
        else:
            break
        change("Violet", bold=True)
    a.save("글자4")
    hwp.Clear(1)
    hwp.Quit()


