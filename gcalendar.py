import requests
import ics
import arrow

PRIVATE_ICS_URL = "https://calendar.google.com/calendar/ical/weargoggles.co.uk_ua13rcg16tm2t6c1m3jnpl6h28%40group.calendar.google.com/private-6970f1ae231269334b0d1f81b8f5c9d0/basic.ics"
CALENDAR_ID = "weargoggles.co.uk_ua13rcg16tm2t6c1m3jnpl6h28@group.calendar.google.com"

# https://developers.google.com/google-apps/calendar/v3/reference/events/list

# https://developers.google.com/google-apps/calendar/auth

def get_events():
    with requests.get(PRIVATE_ICS_URL) as response:
        cal = ics.Calendar(response.text)
    
    return cal.events
    
def is_an_event_active():
    events = get_events()
    now = arrow.now()
    return any(e.begin <= now <= e.end for e in events)


if __name__ == "__main__":
    now = arrow.now()
    print("events now:", list(e for e in get_events() if e.begin <= now <= e.end))
