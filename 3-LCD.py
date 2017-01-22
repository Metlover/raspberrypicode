import RPi.GPIO as gpio
import LCD.hd44780 as LCD
#import gpiozero as GPIO
import sys
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)
gpio.setup(2, gpio.OUT)
p = gpio.PWM(21, 50)
lcd = LCD.HD44780()
#led = GPIO.LED(2)

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': ' ',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
def buzz(pitch, duration):
	period = 1.0 / pitch
	delay = period / 2
	cycles = int(duration * pitch)
	print(period, delay, cycles)
	for i in range(cycles):
		gpio.output(21, True)
		sleep(delay)
		gpio.output(21, False)
		sleep(delay)

def main():
	#print(sys.argv)
	#print(len(sys.argv))
	if len(sys.argv) == 1:
		msg = raw_input("MESSAGE: ")
	else:
		#print(sys.argv[1])
		msg = " ".join(sys.argv[1:])
	#print(msg)
	lcd.clear()
	lcd.message(msg.upper())
	for char in msg:
		message =  CODE[char.upper()]
		
		for char in message:
			#print(char)
			if char == ".":
				#print("about to turn on")
				p.start(100)
				gpio.output(2, gpio.HIGH)
				#print("about to sleep")
				sleep(0.2)
				#print("about to turn off")
				p.stop()
				gpio.output(2, gpio.LOW)
			elif char == "-":
				#print("about to turn on")
				p.start(100)
				gpio.output(2, gpio.HIGH)
				#print("about to sleep")
				sleep(0.8)
				#print("about to turn off")
				p.stop()
				gpio.output(2, gpio.LOW)
			else:
				sleep(0.5)
			sleep(1)
			#print("sleeping")
	#led.close()
	lcd.clear()
	gpio.cleanup()
		
if __name__ == "__main__":
	try:
		main()
	except:
		lcd.clear()
		gpio.cleanup()
		#led.close()
