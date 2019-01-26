import sys
import autopy
import time
import finder
import random
from keras.utils import to_categorical
#Set location to top corner to start
#These values are determined by screen size and window size

class jewlsim():

    def __init__(self):
        self.board, self.leterboard = self._gen_board()

    def _gen_board(self):
        board = []
        leterboard = []
        for i in range(0,8):
            row = []
            for j in range(0,8):
                row.append(random.randrange(0,7))
            board.append(row)
        for row in board:
            for gem in row:
                lrow=[]
                if gem == 0:
                    lrow.append('w')
                elif gem == 1:
                    lrow.append('o')
                elif gem == 2:
                    lrow.append('g')
                elif gem == 3:
                    lrow.append('y')
                elif gem == 4:
                    lrow.append('b')
                elif gem == 5:
                    lrow.append('p')
                elif gem == 6:
                    lrow.append('r')
                else:
                    lrow.append('x')
                leterboard.append(lrow)
        board = to_categorical(board)
        update = []
        i = 0
        for r in board:
            row = []
            j = 0
            for g in r:
                row.append([i,j,g])
                j+=1
            i+=1
            update.append(row)
        print(update)
        return board, leterboard

    def create_board(self):
        return self.board


    def move_up(xcor,ycor):
        return

    def move_down(xcor,ycor):
        return

    def move_left(xcor,ycor):
        return

    def move_right(xcor,ycor):
        return
    #adjust these
    def _check_left(xcor, ycor, leterboard):
        gem = leterboard[ycor][xcor]
        #Check up
        matches = 0
        done = False
        yl = ycor
        while done == False and yl >= 1:
            up = leterboard[yl-1][xcor-1]
            if up == gem or up == 'x':
                matches += 1
                yl -= 1
            else:
                done = True
        if matches >= 2:
            return True
        #check bottom side for matches
        done = False
        yl = ycor
        while done == False and yl <= 6:
            up = leterboard[yl+1][xcor-1]
            if up == gem or up == 'x':
                matches += 1
                yl += 1
            else:
                done = True
        if matches >= 2:
            return True
        #Check Left side for matches
        matches = 0
        done = False
        xl = xcor-1
        while done == False and xl >= 1:
            left = leterboard[ycor][xl-1]
            if left == gem or left == 'x':
                matches += 1
                xl -= 1
            else:
                done = True
        if matches >= 2:
            return True
        return False

    def _check_right(xcor, ycor, leterboard):
        gem = leterboard[ycor][xcor]
        #Check up
        matches = 0
        done = False
        yl = ycor
        while done == False and yl >= 1:
            up = leterboard[yl-1][xcor+1]
            if up == gem or up == 'x':
                matches += 1
                yl -= 1
            else:
                done = True
        if matches >= 2:
            return True
        #check bottom side for matches
        done = False
        yl = ycor
        while done == False and yl <= 6:
            up = leterboard[yl+1][xcor+1]
            if up == gem or up == 'x':
                matches += 1
                yl += 1
            else:
                done = True
        if matches >= 2:
            return True
        #check Right side for matches
        done = False
        matches = 0
        xr = xcor+1
        while done == False and xr <= 6:
            right = leterboard[ycor][xr+1]
            if right == gem or right == 'x':
                matches += 1
                xr += 1
            else:
                done = True
        if matches >= 2:
            return True

        return False

    def _check_up(xcor, ycor, leterboard):
        gem = leterboard[ycor][xcor]
        if ycor == 0:
            return False
        #Check Left side for matches
        matches = 0
        done = False
        xl = xcor
        while done == False and xl >= 1:
            left = leterboard[ycor-1][xl-1]
            if left == gem or left == 'x':
                matches += 1
                xl -= 1
            else:
                done = True
        if matches >= 2:
            return True
        #check Right side for matches
        done = False
        xr = xcor
        while done == False and xr <= 6:
            right = leterboard[ycor-1][xr+1]
            if right == gem or right == 'x':
                matches += 1
                xr += 1
            else:
                done = True
        if matches >= 2:
            return True
        #check Top side for matches
        matches = 0
        done = False
        yl = ycor-1
        while done == False and yl >= 1:
            up = leterboard[yl-1][xcor]
            if up == gem or up == 'x':
                matches += 1
                yl -= 1
            else:
                done = True
        if matches >= 2:
            return True
        return False

    def _check_down(xcor, ycor, leterboard):
        gem = leterboard[ycor][xcor]
    #Downwards movement
        matches = 0
        done = False
        xl = xcor
        while done == False and xl >= 1:
            left = leterboard[ycor+1][xl-1]
            if left == gem or left == 'x':
                matches += 1
                xl -= 1
            else:
                done = True
        if matches >= 2:
            return True
        #check Right side for matches
        done = False
        xr = xcor
        while done == False and xr <= 6:
            right = leterboard[ycor+1][xr+1]
            if right == gem or right == 'x':
                matches += 1
                xr += 1
            else:
                done = True
        if matches >= 2:
            return True
        #check bottom side for matches
        matches = 0
        done = False
        yl = ycor+1
        while done == False and yl <= 6:
            up = leterboard[yl+1][xcor]
            if up == gem or up == 'x':
                matches += 1
                yl += 1
            else:
                done = True
        if matches >= 2:
            return True

        return False

    def check_move(xcor, ycor, dir, leterboard):
        gem = leterboard[ycor][xcor]
        if gem == 'x':
            return True
        if ycor == 0 and dir == 0:
            return False
        if ycor == 7 and dir == 2:
            return False
        if xcor == 0 and dir == 1:
            return False
        if xcor == 7 and dir == 3:
            return False
        if dir == 0:
            return _check_up(xcor, ycor, leterboard) or _check_down(xcor, ycor-1, leterboard)
        if dir == 1:
            return _check_left(xcor, ycor, leterboard) or _check_right(xcor-1, ycor, leterboard)
        if dir == 2:
            return _check_up(xcor, ycor+1, leterboard) or _check_down(xcor, ycor, leterboard)
        if dir == 3:
            return _check_left(xcor+1, ycor, leterboard) or _check_right(xcor, ycor, leterboard)

        return False
