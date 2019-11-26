import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import urllib2
import time

myAPI = "MJ0CC8EH8NFH4TCV"

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23)
    return (str(RH), str(T))
def main2():
    print("starting...")
    baseURL = "https://api.thingspeak.com/update?api_key=%s" % myAPI
    while True:
        try:        
            RH, T = getSensorData()
            f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (T, RH))
            print (f.read())
            f.close()
            print("%s : %s" % (T,RH))
            time.sleep(300)
        except:
            print("exiting")
            break
if __name__ == "__main__":
    main2()


