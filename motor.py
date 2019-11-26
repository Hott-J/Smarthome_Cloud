import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#pin number set
motor_pin = 12

#output pin set
GPIO.setup(motor_pin,GPIO.OUT)
        
freq = 100
deg_min = 0.0
deg_max = 90.0
dc_min = 5.0
dc_max = 22.0


p = GPIO.PWM(motor_pin,freq)
p.start(0)
 
def convert_dc(deg):
    return ((deg-deg_min)*(dc_max-dc_min)/(deg_max-deg_min)+dc_min)

def open_door():
    dc = convert_dc(float(90))
    p.ChangeDutyCycle(dc)
def close_door():
    dc = conver_dc(float(0))
    p.ChangeDutyCycle(dc)
    
    

#@app.route('/open')
#def opendoor():
#    Motor.open_door()
#    GPIO.cleanup()
#    return(''),204
#@app.route('/close')
#def closedoor():
#    Motor.close_door()
#    GPIO.claenup()
#    return(''),204

open_door()
GPIO.cleanup()