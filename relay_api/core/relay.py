import RPi.GPIO as GPIO

class relay():
    def __init__(self, gpio_num, relay_type="NO"):
        self.gpio_num = gpio_num
        GPIO.setmode(GPIO.BCM)
        try:
            GPIO.input(self.gpio_num)
            raise LookupError("Relay is already in use!")
        except RuntimeError:
            GPIO.setup(self.gpio_num, GPIO.OUT)
        except ValueError:
            raise LookupError("Relay number invalid!")
        if relay_type == "NC":
            self.on()
        else:
            self.off()

    def on(self):
        GPIO.output(self.gpio_num, GPIO.HIGH)

    def off(self):
        GPIO.output(self.gpio_num, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup(self.gpio_num)
