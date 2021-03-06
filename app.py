import os
from flask import Flask, request, g
from flask_cors import CORS

from server.views.home_view import HomeView
from server.views.led_api_view import ActivateLEDView

from led_control.led_controller import LEDController

# The Flask app
app = Flask(__name__, template_folder='server/templates')
# Enable CORS app-wide
CORS(app)

# The mapping from keys to GPIO pins
# This should reflect the physical LED circuit
#   attached to the nametag
LED_MAPPING = {
    'whoami': 18,
    'ls -l /home/mike/work': 15,
    'sudo rm -rf /bad/vibes': 14
}


# Before each request, add an LEDController to Flasks "global"
#   g variable
# This is a poor-man's dependency injection, but eh
@app.before_request
def before_request_prepare():
    led_controller = LEDController(LED_MAPPING)
    led_controller.activate()
    g.led_controller = led_controller


app.add_url_rule('/home', view_func=HomeView.as_view('home_view'))
app.add_url_rule('/activateLED', view_func=ActivateLEDView.as_view('led_api_view'))




if __name__ == '__main__':
    port = 8080
    print("Now running Flask Server out of port %s" % port) 
    app.run(port=port, host='0.0.0.0')
