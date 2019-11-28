from flask import Flask, render_template, request 
import RPi.GPIO as GPIO     
from time import sleep      
 

servo = 26          

 
GPIO.setmode(GPIO.BOARD)      

GPIO.setup(servo, GPIO.OUT)     

 

p = GPIO.PWM(servo, 100)

 

p.start(0)

 

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('motor.html')
 
@app.route("/test", methods=["POST"])
def test():

    slider1 = request.form["slider1"]

    p.ChangeDutyCycle(float(slider1))

    sleep(1)
    p.ChangeDutyCycle(0)
    return render_template('motor.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
