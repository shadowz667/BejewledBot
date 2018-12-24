import sys
import autopy
print("Hello Atom")
screen = autopy.bitmap.capture_screen(None)
blue = autopy.bitmap.Bitmap.open('BejewledBot\\gems\\red.PNG')
#loc = screen.find_every_bitmap(blue,.25)
#print(loc)
x = 462.0+55.5
y = 93.0+55.5
autopy.mouse.move(x,y)
autopy.mouse.move(x+111,y)
#print(autopy.mouse.location())
