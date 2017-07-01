import RPi.GPIO as GPIO

MAX_RELAY_GPIO = 27


class relay():
    def __init__(self, gpio_num):
        if gpio_num not in range(MAX_RELAY_GPIO + 1):
            raise LookupError("Relay GPIO invalid! Use one between 0 - " +
                              str(MAX_RELAY_GPIO))

        self.gpio = gpio_num
        GPIO.setmode(GPIO.BCM)

        try:
            GPIO.input(self.gpio)
            raise LookupError("Relay GPIO is already in use!")
        except RuntimeError:
            GPIO.setup(self.gpio, GPIO.OUT)

        self.off()

    def on(self):
        GPIO.output(self.gpio, GPIO.HIGH)
        self.state = True

    def off(self):
        GPIO.output(self.gpio, GPIO.LOW)
        self.state = False

    def get_state(self):
        return self.state

    def cleanup(self):
        GPIO.cleanup(self.gpio)
