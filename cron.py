import switch
from gauge import temperature
from gcalendar import is_event_active
from thermastat import get_bounds

if __name__ == "__main__":
    event_active = is_event_active()
    lower, upper = get_bounds(event_active)

    if temperature() > upper:
        switch.off()

    if temperature() < lower:
        switch.on()
