import os
from flask import Flask, request, g
from flask_cors import CORS

from server.views.home_view import HomeView
from server.views.led_api_view import TempLEDView

from led_control.led_controller import LEDController

# The Flask app
app = Flask(__name__, template_folder='server/templates')
# Enable CORS app-wide
CORS(app)

# The mapping from keys to GPIO pins
# This should reflect the physical LED circuit
#   attached to the nametag
LED_MAPPING = {
    'ls': 18,
    'rm': 15
}


# Before each request, add an LEDController to Flasks "global"
#   g variable
# This is a poor-man's dependency injection, but eh
@app.before_request
def before_request_prepare():
    led_controller = LEDController(LED_MAPPING)
    led_controller.activate()
    g.led_controller = led_controller


# TODO: add API endpoints using Flask Views
app.add_url_rule('/home', view_func=HomeView.as_view('home_view'))
app.add_url_rule('/activateLED/<led_key>', view_func=TempLEDView.as_view('led_api_view'))




if __name__ == '__main__':
    port = 8080
    print("Now running Flask Server out of port %s" % port) 
    app.run(port=port, host='0.0.0.0')
