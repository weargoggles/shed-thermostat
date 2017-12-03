#!/usr/bin/env python2
from gpiozero import Energenie
import sys


def on():
    with Energenie(1) as heater:
        heater.on()


def off():
    with Energenie(1) as heater:
        heater.off()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("tell me on or off")
        sys.exit(1)
    on() if sys.argv[1] == "on" else off()
