import sys
import autopy
print("Hello Atom")
screen = autopy.bitmap.capture_screen(None)
#Set location to top corner to start
#These values are determined by screen size and window size
x = 462.0+55.5
y = 93.0+55.5


def create_board():
    board = []
    for i in range(0,8):
        row = []
        for j in range(0,8):
            row.append(screen.get_color(x+(j*111),y+(i*111)))
        board.append(row)
        print(row)
    return board
autopy.mouse.move(x+777,y+777)
autopy.mouse.click()
autopy.mouse.move(x+777,y+666)
autopy.mouse.click()
#print(autopy.mouse.location())
