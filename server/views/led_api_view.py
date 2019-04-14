from flask import g, request
from flask.views import MethodView


class ActivateLEDView(MethodView):
    def post(self):
        request_json = request.get_json()

        led_key = request_json.get('led_key', None)
        duration = request_json.get('duration', 2)

        # Maximum of 5 seconds for duration
        if duration > 5:
            duration = 5


        if led_key is None:
            return "Malformed request JSON", 400

        print("Turning on LED for key %s" % led_key)
        led_controller = g.led_controller
        led_activated_success = led_controller.turn_on_led(led_key, duration=duration)

        if led_activated_success:
            return "Successfully turned on LED"
        else:
            return "Failed to turn on LED", 500

