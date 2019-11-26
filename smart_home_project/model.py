from peewee import*
import Adafruit_DHT

db=SqliteDatabase('dht.db',check_same_thread=False)

class DHTSensor(Model):
    name=CharField()
    dht_type=IntegerField()
    pin=IntegerField()
    
    class Meta:
        database=db
    
class SensorReading(Model):
    time=DateTimeField()
    name=CharField()
    value=FloatField()
    
    class Meta:
        database=db
        
class DHTData(object):
    def __init__(self):
        db.connect()
        db.create_tables([DHTSensor,SensorReading],safe=True)
        
    def define_sensor(self,name,dht_type,pin):
        DHTSensor.get_or_create(name=name,dht_type=dht_type,pin=pin)
        
    def get_sensor(self):
        return DHTSensor.select()
    
    def get_recent_readings(self,name,limit=30):
        return SensorReading.select(),where(SensorReading.name==name).order_by(SensorReading.time)
    
    def add_reading(self,time,name,value):
        SensorReading.create(time=time,name=name,value=value)
        
    def close(self):
        db.close()
    
class Pithing(object):
    def get_humidity(self):
        humidity,temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,2)
        return humidity
    
    def get_temperature(self):
        humidity,temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,2)
        return temperature