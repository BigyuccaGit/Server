'''
	Raspberry Pi GPIO Status and Control
'''
from gpiozero import LED
from flask import Flask, render_template, request

app = Flask(__name__)

#define actuators GPIOs
leftLedPin = 20
rightLedPin = 14

 
# turn leds OFF 

leftLed=LED(leftLedPin)
rightLed=LED(rightLedPin)

#initialize GPIO status variables
leftLed.off()
rightLed.off()
leftLedSts = leftLed.value
rightLedSts = rightLed.value
	
@app.route("/")
def index():
	# Read Sensors Status
	leftLedSts = leftLed.value 
	rightLedSts = rightLed.value
	templateData = {
              'title' : 'GPIO output Status!',
              'leftLed'  : leftLedSts,
              'rightLed'  : rightLedSts,
        }
	return render_template('led.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    
	if deviceName == 'leftLed':
		actuator = leftLed
	if deviceName == 'rightLed':
		actuator = rightLed

   
	if action == "on":
		actuator.on()
	if action == "off":
		actuator.off()
		     
	leftLedSts = leftLed.value
	rightLedSts = rightLed.value
   
	templateData = {
              'leftLed'  : leftLedSts,
              'rightLed'  : rightLedSts,
	}
	return render_template('led.html', **templateData)
    
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
