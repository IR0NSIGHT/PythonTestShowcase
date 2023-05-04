from typing import Tuple, Dict

Rect = Tuple[float, float]

def makeRect(x: float, y: float) -> Rect:
    return (x,y)

def rectArea(r: Rect):
    return r[0] * r[1]

def makeSquare(x: float) -> Rect:
    return (x,x)

def owo():
    return 1
