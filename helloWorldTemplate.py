'''
Code created by Matt Richardson 
for details, visit:  http://mattrichardson.com/Raspberry-Pi-Flask/inde...
'''
from flask import Flask, render_template
import datetime

# Create a Flask object
app = Flask(__name__)

# Run index function when someone accesses the root URL ('/') of the server
@app.route("/")
def hello():
   # Info for display
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   # Render template in templates dir
   return render_template('index.html', **templateData)

# Listen on port 80
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
