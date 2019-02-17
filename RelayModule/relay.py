import RPi.GPIO as GPIO
import time

relayPin = 18 # pin 18

# initialize GPIO
def setup():
	GPIO.setmode(GPIO.BCM) # numbers GPIOs by physical location
	GPIO.setup(relayPin,GPIO.OUT) # Set relayPin's mode is outpu
	GPIO.output(relayPin,GPIO.HIGH) # Set relayPin high (+5V) to off led
	time.sleep(10)

def loop():
	while True:
		print ("Relay  on")
		GPIO.output(relayPin,GPIO.LOW) # relay on 
		time.sleep(10)
		print ("Relay off")
		GPIO.output(relayPin,GPIO.HIGH) # relay off
		time.sleep(10)

def destroy():
	GPIO.output(relayPin,GPIO.HIGH) # led off
	GPIO.cleanup() # release resource

if __name__ == '__main__': # program starts here
	setup()
	try:
		loop()
	except KeyboardInterrupt: # when 'CTL+C' is pressed, the child program destroy will be executed.
		destroy()


