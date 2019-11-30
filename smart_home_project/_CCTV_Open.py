from flask import Flask, render_template, request, Response 
import RPi.GPIO as GPIO     
from time import sleep      
from camera import Camera 

servo = 26          

 
GPIO.setmode(GPIO.BOARD)      

GPIO.setup(servo, GPIO.OUT)     

 

p = GPIO.PWM(servo, 100)

 

p.start(0)

 

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('CCTV_Open.html')

@app.route("/test", methods=["POST"])
def test():

    slider1 = request.form["slider1"]

    p.ChangeDutyCycle(float(slider1))

    sleep(1)
    p.ChangeDutyCycle(0)
    return render_template('CCTV_Open.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)