import RPi.GPIO as GPIO
from datetime import datetime
import Adafruit_DHT
import time

from model import DHTData

data=DHTData()

data.define_sensor('DHT2',Adafruit_DHT.DHT22,2)

led=11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)

humidity,temperature=Adafruit_DHT.read_retry(22,2)

try:
    while True:
        reading_time=datetime.now()
        for sensor in data.get_sensor():
            humidity,temperature=Adafruit_DHT.read_retry(sensor.dht_type,sensor.pin)
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

            if humidity is not None and temperature is not None:
                if temperature >=27:
                    GPIO.output(led,1)
            
                elif temperature <=17:
                    GPIO.output(led,1)
                else:
                    GPIO.output(led,1)
            data.add_reading(reading_time,'{0} Humidity'.format(sensor.name),humidity)
            data.add_reading(reading_time,'{0} temperature'.format(sensor.name),temperature)
        time.sleep(2.0)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    data.close()