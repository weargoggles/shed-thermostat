import switch
from gauge import temperature


if __name__ == "__main__":
    if temperature() > 18:
        switch.off()

    if temperature() < 16:
        switch.on()