import sys
import autopy
import time
from PIL import Image
import pytesseract
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
def get_score():
    autopy.bitmap.capture_screen(((130,170),(190,50))).save("BejewledBot\\screencaps\\score.png","png")
    score = pytesseract.image_to_string("BejewledBot\\screencaps\\score.png")
    if(score == ''):
        return 0
    score = score.split(',')
    score2 = ''
    for s in score:
        score2 = score2+s
    return int(score2)
