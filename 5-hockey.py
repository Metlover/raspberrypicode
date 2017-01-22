import urllib2
from time import sleep
import json
from collections import namedtuple
import RPi.GPIO as gpio
import LCD.hd44780 as LCD
import sys

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)
lcd = LCD.HD44780()

try:
	while True:
		scoresheetRaw = urllib2.urlopen('http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp')
		jsonfile = scoresheetRaw.read()
		jsonfile = jsonfile[len('loadScoreboard('):-1]
		x = json.loads(jsonfile, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
		for game in x.games:
			output = game.atv + ' ' + game.hts + '\n' + game.htv + ' ' + game.ats + '   ' + game.bs
			lcd.clear()
			lcd.message(output.upper())
			sleep(5)
finally:
	lcd.clear()
	gpio.cleanup()
