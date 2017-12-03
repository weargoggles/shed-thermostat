import arrow
import logging
import switch
from gauge import temperature
from gcalendar import is_an_event_active
from thermostat import get_bounds


logging.captureWarnings(True)


if __name__ == "__main__":
    event_active = is_an_event_active()
    lower, upper = get_bounds(event_active)
    t = temperature()
    action = ""

    if t > upper:
        switch.off()
        action = "Off"

    if t < lower:
        switch.on()
        action = "On"
    
    with open("log.csv", "ab") as log:
        log.write(arrow.now().format("YYYY-MM-DD HH:mm:ssZZ"))
        log.write(",")
        log.write(str(t))
        log.write(",")
        log.write(action)
        log.write("\n")
