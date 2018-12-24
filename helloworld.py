import sys
import autopy
print("Hello Atom")

white = autopy.bitmap.Bitmap.open('BejewledBot\\gems\\white.bmp')
white.save('BejewledBot\\high.jpg', 'jpeg')
autopy.bitmap.capture_screen(None).save('BejewledBot\\high.jpg', 'jpeg')
