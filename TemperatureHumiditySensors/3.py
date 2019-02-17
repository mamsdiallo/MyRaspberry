import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sqlite3

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 21
instance = dht11.DHT11(pin=21)

# connect to the database
conn = sqlite3.connect('sensor.db')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS hum(
    t DATETIME,
    hum NUMERIC
)
''')
conn.commit()
cur.execute('''
CREATE TABLE IF NOT EXISTS temp(
    t DATETIME,
    temp NUMERIC
)
''')


while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        now = datetime.datetime.now()
        temp = result.temperature
        print("Temperature: %d C" % temp)
        h = result.humidity
        print("Humidity: %d %%" % h)
        donnees = {"t":now,"temp":temp}
	# write the temperature and the humidity
        cur.execute('''INSERT INTO hum(t,hum) VALUES(?,?)''',(now,h))
	# commit the changes
        conn.commit()
        cur.execute('''INSERT INTO temp(t,temp) VALUES(?,?)''',(now,temp))
        conn.commit()

    time.sleep(1)
