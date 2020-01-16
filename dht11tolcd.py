
import os
import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

os.chdir('/home/pi/Adafruit_Python_CharLCD/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11,cols=16, lines=2)
lcd.clear()
lcd.show_cursor(False)
lcd.blink(False)
lcd.move_left()
lcd.move_right()
lcd.show_cursor(False)

# read data using pin 14
instance = dht11.DHT11(pin=17)

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("Last valid input: " + str(datetime.datetime.now()))

	        print("Temperature: %d C" % result.temperature)
		print("Temperature: %d F" % ((result.temperature * 9/5)+32)) 
		print("Humidity: %-3.1f %%" % result.humidity)
	        lcd.message('Temp: ')
                lcd.message("%d" % result.temperature)
   	        lcd.message('^C\n')
                lcd.message('Humidity: ')
		lcd.message('%d' % result.humidity)
	        lcd.message('% \n')
		time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
