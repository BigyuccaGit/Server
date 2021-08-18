# NOTE: run this as sudo python3  hello-flask.py

# Load the Flask module into your Python script
from flask import Flask

# Create a Flask object called app
app = Flask(__name__)

# Run the code below this function when someone accesses the root URL of the server
@app.route("/")
def hello():
#   Send the text "Hello World!" to the client's web browser
    return "Hello World!"

# Have the server listen on port 80 and report any errors.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

