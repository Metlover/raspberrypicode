from gpiozero import LED
from time import sleep

led = LED(2)
led.off()
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


def main():
	
	msg = raw_input('MESSAGE: ')
	print(msg)
	for char in msg:
		message =  CODE[char.upper()]
		for char in message:
			#print(char)
			if char == ".":
				#print("about to turn LED on")
				led.on()
				#print("about to sleep")
				sleep(0.1)
				#print("about to turn off")
				led.off()
			elif char == "-":
				#print("about to turn LED on")
				led.on()
				#print("about to sleep")
				sleep(0.5)
				#print("about to turn off")
				led.off()
			else:
				#print("sleeping")
				sleep(0.5)
				#print("not sleeping")
			sleep(1)
			#print("sleeping")
		
if __name__ == "__main__":
	try:
		main()
		led.close()
	except:
		led.close()
