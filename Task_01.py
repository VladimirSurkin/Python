# Task_1
import time
from pyfancy.pyfancy import pyfancy

class TrafficLight:

    def running(self):
        while True:
            pyfancy().red("Red light").output()
            time.sleep(7)
            pyfancy().yellow("Yellow light").output()
            time.sleep(2)
            pyfancy().green("Green light").output()
            time.sleep(7)
            pyfancy().yellow("Yellow light").output()
            time.sleep(2)


a = TrafficLight()
a.running()
