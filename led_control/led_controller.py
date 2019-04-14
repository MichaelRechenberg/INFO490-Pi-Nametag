import RPi.GPIO as GPIO
import time

class LEDController:

    def __init__(self, led_mapping):
        """Initialize an LED Controller

            Arguments:
                led_mapping: A dictionary that maps keys to GPIO pin numbers.  
                    The keys in this dictionary can be passed to turn_on_led()
                    to turn on the appropriate LED
        """
        self.led_mapping = led_mapping

        # Flag indicating if an LED is currently active.  Used to 
        #   ensure that only one LED is active at any one time
        self.led_is_active = False 

    def activate(self, gpio_mode=GPIO.BCM):
        """Activate an LED Controller (one-time GPIO initialization)

            Arguments:
                gpio_mode: The GPIO mode to use.  Defaults to RPi.GPIO.BCM.
                    See RPi.GPIO.setmode() for possible values
        """

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)

        for pin_number in self.led_mapping.values():
            GPIO.setup(pin_number, GPIO.OUT)


    def turn_on_led(self, led_key, duration=2.0):
        """Turn on an LED for a specified amount of time (seconds),
            then turn off the LED

            The current implementation of this function busy waits while the
                LED is turned on

            Arguments:
                led_key: The key for the LED (the key within the led mapping passed
                    to LEDController's constructor)
                duration: (Optional) The number of seconds to keep the LED on
        """

        pin_number = self.led_mapping.get(led_key, None)

        if pin_number is None:
            # The key did not match any of the registered LED keys 
            return False

        GPIO.output(pin_number, GPIO.HIGH)
        # NOTE: time.sleep() halts the current thread.  Perhaps if we wanted 
        #   to return control to the caller faster, we could spawn a new thread
        #   to handle the LEDs
        time.sleep(duration)
        GPIO.output(pin_number, GPIO.LOW)

        return True




