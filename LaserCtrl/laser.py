import RPi.GPIO as GPIO
import time

LedPin = 18 # pin 18

# initialize GPIO
def setup():
	GPIO.setmode(GPIO.BCM) # numbers GPIOs by physical location
	GPIO.setup(LedPin,GPIO.OUT) # Set ledPin's mode is outpu
	GPIO.output(LedPin,GPIO.HIGH) # Set LedPin high (+5V) to off led

def loop():
	while True:
		print ("laser  on")
		GPIO.output(LedPin,GPIO.LOW) # led on 
		time.sleep(0.5)
		print ("Laser off")
		GPIO.output(LedPin,GPIO.HIGH) # led off
		time.sleep(0.5)

def destroy():
	GPIO.output(LedPin,GPIO.HIGH) # led off
	GPIO.cleanup() # release resource

if __name__ == '__main__': # program starts here
	setup()
	try:
		loop()
	except KeyboardInterrupt: # when 'CTL+C' is pressed, the child program destroy will be executed.
		destroy()


