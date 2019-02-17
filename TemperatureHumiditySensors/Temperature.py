import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sqlite3

# initialize GPIO
def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()
	# perform SQL commands
	# save (commit) the changes
	cur.execute('''
	CREATE TABLE IF NOT EXISTS temp(
    		t DATETIME,
    		temp NUMERIC,
		sensorid INTEGER
	)
	''')
	# save (commit) the changes
	conn.commit()


def loop():
	while True:
		time.sleep(1)
		result = instance.read()
		if result.is_valid():
			print("Last valid input: " + str(datetime.datetime.now()))
			now = datetime.datetime.now()
			temp = result.temperature
			print("Temperature: %d C" % temp)
			id = 1
			donnees = {"t":now,"temp":temp,"sensorid":id}
			# write the temperature
			cur.execute('''INSERT INTO temp(t,temp,sensorid) VALUES(?,?,?)''',(now,temp,id))
			# commit the changes
			conn.commit()

def destroy():
	# we are done with the dataabse, close the connection
	conn.close()
	GPIO.cleanup() # release resource

if __name__ == '__main__': # program starts here
	# read data using pin 21
	instance = dht11.DHT11(pin=21)
	# connect to the database
	conn = sqlite3.connect('sensor.db')
	# create a cursor object 
	cur = conn.cursor()
	setup()
	try:
		loop()
	except KeyboardInterrupt: # when 'CTRL+C' is pressed', the child program destroy will be executed.
		destroy()

 
