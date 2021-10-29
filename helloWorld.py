from flask import Flask

# Create a Flask object
app = Flask(__name__)

# Run index function when someone accesses the root URL ('/') of teh server
@app.route('/')
def index():
    return 'Hello world'

# Listen on port 80
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
