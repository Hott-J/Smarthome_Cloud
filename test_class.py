import RPi.GPIO as GPIO

class Motor(object):
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
        return ((deg-Motor.deg_min)*(Motor.dc_max-Motor.dc_min)/(Motor.deg_max-Motor.deg_min)+Motor.dc_min)
    
    def open_door():
        dc = Motor.convert_dc(float(90))
        Motor.p.ChangeDutyCycle(dc)
        GPIO.cleanup()
        
    def close_door():
        dc = Motor.conver_dc(float(0))
        Motor.p.ChangeDutyCycle(dc)
        GPIO.cleanup()
    
        
        