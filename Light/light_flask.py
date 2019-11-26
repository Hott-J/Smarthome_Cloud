from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

leds = {
23 : {'name' : 'Light', 'state' : GPIO.LOW}
}

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.OUT)

def getGpioState():
    for led in leds:
        leds[led]['state']=GPIO.input(led)
    return leds

@app.route("/")
def main():
    gpioState = {
         'leds' : getGpioState()
    }

    return render_template('main.html', **gpioState)

@app.route("/<led>/<act>")
def action(led, act):
    led = int(led)
    leds = getGpioState()
    dev = leds[led]['name']
    if act == "on":
        GPIO.output(led, GPIO.HIGH)
        msg = "Light is " + dev + " on. "
    elif act == "off":
        GPIO.output(led, GPIO.LOW)
        msg = "Light is " + dev + " off. "
    elif act == "toggle":
        GPIO.output(led, not GPIO.input(led))
        msg = "Toggled " + dev + "."
    else:
        msg = "Undefined action!"

    gpioState = {
        'msg' : msg,
        'leds' : getGpioState()
    }

    return render_template('main.html', **gpioState)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000, debug=True)

