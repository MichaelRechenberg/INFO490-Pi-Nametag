from flask import g
from flask.views import MethodView

class TempLEDView(MethodView):
    def get(self, led_key):

        led_controller = g.led_controller

        print("Attempting to activate the LED for key %s" % led_key)

        led_controller.turn_on_led(led_key, duration=2)

        return "Done"
