import sys
import autopy
import time
from PIL import Image
import pytesseract
# If you don't have tesseract executable in your PATH, include the following:
#normal mode
x1 = 130
y1 = 170
x2 = 190
y2 = 50
#zen mode
#x1,y1 = 137.0, 101.0
#x2,y2 = 309.0-x1, 157.0-y1

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Lucas\Downloads\tesseract-Win64\tesseract'
def get_score():
    autopy.bitmap.capture_screen(((x1,y1),(x2,y2))).save("screencaps\\score.png","png")
    score = pytesseract.image_to_string("screencaps\\score.png", config=" -c tessedit_char_whitelist=0123456789")
    #print(score)
    if(score == ''):
        return 0
    score = score.split(' ')
    score2 = ''
    for s in score:
        score2 = score2+s
    try:
        return int(score2)
    except:
        return -1
