import GPi.GPIO as GPIO
import tkinter as tk
import time


GPIO.setmode(GPIO.BOARD)

pin = 13

GPIO.setup(pin,GPIO.OUT)

freq = 100.0
deg_min = 0.0
deg_max = 90.0
dc_min = 5.0
dc_max = 22.0

p = GPIO.PWM(pin,freq)
p.start(0)


window = tk.Tk()
def convert_dc(deg):
    return (deg - deg_min)*(dc_max - dc_min)/(deg_max - deg_min)+dc_min

def open_door():
    for deg in range(0,91,1):
        dc = convert_dc(float(deg))
        p.ChangeDutyCycle(dc)
        ## 동작하는 거 보고 sleep넣어주세요

def close_door():
    for deg in range(90,-1,-1):
        dc = convert(dc)
        p.ChangeDutyCycle(dc)

button1=tk.Button(window,text='OPEN',command = open_door)
button2=tk.Button(window,text = "CLOSE",command = close_door)

button1.pack(side='left')
button2.pack(side='right')
window.mainloop()
GPIO.cleanup()
