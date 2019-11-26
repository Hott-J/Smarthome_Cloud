from flask import Flask
from flask_admin import Admin
from flask_admin import BaseView,expose
from flask_admin.contrib.peewee import ModelView
from flask import *

import model
import time
import json

class MyView(BaseView):
    @expose('/smarthome')
    def index(self):
        return self.render('temp.html')

tempapp=Flask(__name__)
tempapp.config['SECRET_KEY']='20150333'
tempapp.config['MODEL']=model.DHTData()

admin=Admin(tempapp,name='SQLite Sensors',template_mode='bootstrap3',url='/smarthome')

admin.add_view(ModelView(model.DHTSensor))
admin.add_view(ModelView(model.SensorReading))

if __name__ == '__main__':
    tempapp.run()

