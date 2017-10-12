#!/usr/bin/env python2
from gpiozero import Energenie
import sys

def heater(on):
  with Energenie(1) as heater:
    heater.on() if on else heater.off()


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("tell me on or off")
    sys.exit(1)
  heater(sys.argv[1] == "on")
