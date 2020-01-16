import os
os.chdir('/home/pi/Adafruit_Python_CharLCD/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11,cols=16, lines=2)
lcd.clear()
lcd.show_cursor(True)
lcd.blink(True)
lcd.move_left()
lcd.move_right()
lcd.show_cursor(False)
lcd.message('Hi Manish')
