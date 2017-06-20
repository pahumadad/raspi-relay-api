import RPi.GPIO as GPIO


class relay():
    def __init__(self, gpio_num, NC=False):
        self.gpio = gpio_num
        self.nc = NC
        GPIO.setmode(GPIO.BCM)
        try:
            GPIO.input(self.gpio)
            raise LookupError("Relay is already in use!")
        except RuntimeError:
            GPIO.setup(self.gpio, GPIO.OUT)
        except ValueError:
            raise LookupError("Relay number invalid!")
        if self.nc:
            self.on()
        else:
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
