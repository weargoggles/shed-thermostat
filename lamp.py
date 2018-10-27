#!/usr/bin/env python2
from gpiozero import Energenie
import sys


def on():
    with Energenie(3) as device:
        device.on()


def off():
    with Energenie(3) as device:
        device.off()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("tell me on or off")
        sys.exit(1)
    on() if sys.argv[1] == "on" else off()
