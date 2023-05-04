from geometry.square import makeRect, rectArea, Rect

def main():
    print("hello world")
    x = 5
    y = 6
    rect: Rect = makeRect(x,y)
    print("area of rect: "+ str(rect) + " = " + str(rectArea(rect)))

if __name__ == "__main__":
    main()
    
# https://docs.pytest.org/en/7.3.x/