import RPi.GPIO as GPIO
import tkinter as tk

import time
GPIO.setmode(GPIO.BOARD)

srv = 13

GPIO.setup(srv,GPIO.OUT)

freq = 100.0
deg_min = 0.0
deg_max = 90.0
dc_min = 5.0
dc_max = 22.0

p = GPIO.PWM(srv,freq)
p.start(0)

root = tk.Tk()

deg = tk.DoubleVar()
deg.set(0)

def convert_dc(dum):
    dc = (deg.get() - deg_min)*(dc_max - dc_min)/(deg_max - deg_min)+dc_min
    p.ChangeDutyCycle(dc)
    
s = tk.Scale(root,label='angle',orient='h',\
             from_=0,to=90,variable=deg,command=convert_dc)

s.pack()
root.mainloop()

p.stop()
GPIO.cleanup()

            