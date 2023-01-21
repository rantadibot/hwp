from start2 import hwp

def char(color):
    hwp.Run(f"CharShapeTextColor{color.capitalize()}")
def char2(effect):
    hwp.HAction.Run(f"CharShape{effect.capitalize()}")    
def char3(effect):
    hwp.HAction.Run(f"Break{effect.capitalize()}")    


