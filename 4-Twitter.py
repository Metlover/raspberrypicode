import tweepy
from time import sleep
import requests
import RPi.GPIO as gpio
import LCD.hd44780 as LCD
import sys

requests.packages.urllib3.disable_warnings()
auth = tweepy.OAuthHandler("aJPaAv0ii8wov9gWSN0654iCV", "FDgMM8vgoqPCeeJ3LuGvSxUkGskpdMYkhUTVYH0njt3MOpiRre")
auth.set_access_token("3326127862-WWhgFJ14YzeZ4ojo3rS5bqKIrTnFxf1OrseQTGB", "QYLlhFeoK9X4YMSbA0q4oJ0Gdj2DwNvUHAdXTf75icfNQ")
api = tweepy.API(auth)

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)
gpio.setup(2, gpio.OUT)
p = gpio.PWM(21, 50)
lcd = LCD.HD44780()
gpio.output(2, gpio.LOW)

try:
	previousTweet = ""
	searchTerm = raw_input("Insert a search term here. ")
	while True:
		latestTweet = tweepy.Cursor(api.search, q=searchTerm).items(1)
		for tweet in latestTweet:
			TwitterText = tweet.text.encode('utf-8')
			user = tweet.user.screen_name.encode('utf-8')
			#print(TwitterText)
	
		#firstWord = TwitterText.split()[1].strip()
		#print(firstWord)
		newTweet = " ".join(TwitterText.split())
		print(newTweet)
		if previousTweet != newTweet:	
			for i in range(3):
				p.start(100)
				gpio.output(2, gpio.HIGH)
				sleep(0.1)
				p.stop()
				gpio.output(2, gpio.LOW)
				sleep(0.1)
			previousTweet = newTweet
		msg = newTweet + "\n@" + user
		lcd.clear()
		lcd.message(msg)
		sleep(0.3)
		i = 1
		while len(newTweet) - i >= 16:
			msg = newTweet[i: i + 16] + "\n@" + user
			lcd.clear()
			lcd.message(msg)
			i += 1
			sleep(0.3)
	       	sleep(5)

	lcd.clear()
	gpio.cleanup()
except:
	lcd.clear()
	gpio.cleanup()
