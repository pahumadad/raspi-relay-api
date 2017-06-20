import RPi.GPIO as GPIO


class relay():
    def __init__(self, gpio_num, NC=False):
        self.gpio_num = gpio_num
        GPIO.setmode(GPIO.BCM)
        try:
            GPIO.input(self.gpio_num)
            raise LookupError("Relay is already in use!")
        except RuntimeError:
            GPIO.setup(self.gpio_num, GPIO.OUT)
        except ValueError:
            raise LookupError("Relay number invalid!")
        if NC:
            self.on()
        else:
            self.off()

    def on(self):
        GPIO.output(self.gpio_num, GPIO.HIGH)

    def off(self):
        GPIO.output(self.gpio_num, GPIO.LOW)

    def get_state(self):
        return GPIO.input(self.gpio_num)

    def cleanup(self):
        GPIO.cleanup(self.gpio_num)
