import sys
import autopy
import time
import finder
#Set location to top corner to start
#These values are determined by screen size and window size
x = 462.0+55.5
y = 93.0+55.5
#These are the base colors of the gems
white = (253,253,253)
orange = (254,249,130)
green = (88, 252, 142)
yellow = (253, 251, 34)
blue = (18, 130, 251)
purple = (244, 13, 244)
red = (252, 26, 56)

def create_board(tol = 30):
    screen = autopy.bitmap.capture_screen(None)
    board = []
    for i in range(0,8):
        row = []
        for j in range(0,8):
            row.append(screen.get_color(x+(j*111),y+(i*111)))
        board.append(row)
    leterboard = []
    for row in board:
        lrow = []
        #May need to make this smarter to catch specia gems good enough for now
        #Ideas compare multiple boards, look at shape detection
        for gem in row:
            if((gem[0] > (white[0] - tol)) and (gem[0] < (white[0]+tol)) and (gem[1] > (white[1]- tol)) and (gem[1] < (white[1]+tol)) and (gem[2] > (white[2]- tol)) and (gem[2] < (white[2]+tol))):
                lrow.append('w')
            elif((gem[0] > (orange[0] - tol)) and (gem[0] < (orange[0]+tol)) and (gem[1] > (orange[1]- tol)) and (gem[1] < (orange[1]+tol)) and (gem[2] > (orange[2]- tol)) and (gem[2] < (orange[2]+tol))):
                lrow.append('o')
            elif((gem[0] > (green[0] - tol)) and (gem[0] < (green[0]+tol)) and (gem[1] > (green[1]- tol)) and (gem[1] < (green[1]+tol)) and (gem[2] > (green[2]- tol)) and (gem[2] < (green[2]+tol))):
                lrow.append('g')
            elif((gem[0] > (yellow[0] - tol)) and (gem[0] < (yellow[0]+tol)) and (gem[1] > (yellow[1]- tol)) and (gem[1] < (yellow[1]+tol)) and (gem[2] > (yellow[2]- tol)) and (gem[2] < (yellow[2]+tol))):
                lrow.append('y')
            elif((gem[0] > (blue[0] - tol)) and (gem[0] < (blue[0]+tol)) and (gem[1] > (blue[1]- tol)) and (gem[1] < (blue[1]+tol)) and (gem[2] > (blue[2]- tol)) and (gem[2] < (blue[2]+tol))):
                lrow.append('b')
            elif((gem[0] > (purple[0] - tol)) and (gem[0] < (purple[0]+tol)) and (gem[1] > (purple[1]- tol)) and (gem[1] < (purple[1]+tol)) and (gem[2] > (purple[2]- tol)) and (gem[2] < (purple[2]+tol))):
                lrow.append('p')
            elif((gem[0] > (red[0] - tol)) and (gem[0] < (red[0]+tol)) and (gem[1] > (red[1]- tol)) and (gem[1] < (red[1]+tol)) and (gem[2] > (red[2]- tol)) and (gem[2] < (red[2]+tol))):
                lrow.append('r')
            else:
                lrow.append('x')
        leterboard.append(lrow)
#    for l in leterboard:
#        print(l)
    return board


def move_up(xcor,ycor):
    xcor = xcor*111+x
    ycor = ycor*111+y
    if(ycor-111<y):
        return -1
    else:
        autopy.mouse.move(xcor,ycor)
        autopy.mouse.click()
        autopy.mouse.move(xcor,ycor-111)
        autopy.mouse.click()
    autopy.mouse.move(x-100,y)

def move_down(xcor,ycor):
    xcor = xcor*111+x
    ycor = ycor*111+y
    if(ycor+111>y+777):
        return -1
    else:
        autopy.mouse.move(xcor,ycor)
        autopy.mouse.click()
        autopy.mouse.move(xcor,ycor+111)
        autopy.mouse.click()
    autopy.mouse.move(x-100,y)

def move_left(xcor,ycor):
    xcor = xcor*111+x
    ycor = ycor*111+y
    if(xcor-111<x):
        return -1
    else:
        autopy.mouse.move(xcor,ycor)
        autopy.mouse.click()
        autopy.mouse.move(xcor-111,ycor)
        autopy.mouse.click()
    autopy.mouse.move(x-100,y)

def move_right(xcor,ycor):
    xcor = xcor*111+x
    ycor = ycor*111+y
    if(xcor+111>x+777):
        return -1
    else:
        autopy.mouse.move(xcor,ycor)
        autopy.mouse.click()
        autopy.mouse.move(xcor+111,ycor)
        autopy.mouse.click()
    autopy.mouse.move(x-100,y)

def reset_game():
    if finder.get_score() == 0:
        x = 'n'
        while x!='y':
            input(x)
    else:
        autopy.mouse.move(238.0, 918.0)
        autopy.mouse.click()
        autopy.mouse.move(751.0, 814.0)
        time.sleep(1)
        autopy.mouse.click()
        autopy.mouse.move(269.0, 238.0)
        time.sleep(2)
        autopy.mouse.click()
        autopy.mouse.move(841.0, 441.0)
        time.sleep(1)
        autopy.mouse.click()

#for r in create_board():
#    print(r)
