from typing import Tuple, Dict

Rect = Dict[float, float]

def makeRect(x: float, y: float) -> Rect:
    return (x,y)

def rectArea(r: Rect):
    return r[0] * r[1]

