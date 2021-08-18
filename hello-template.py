from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
# Get the current time and store it in the object now
   now = datetime.datetime.now()

# Create a formatted string using the date and time from the now object
   timeString = now.strftime("%Y-%m-%d %H:%M")

# Create a dictionary of variables (a set of keys, such as title that are associated with values, 
# such as HELLO!) to pass into the template
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
# Return the main.html template to the web browser using the variables in the templateData dictionary
   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
