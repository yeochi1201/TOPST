from ..Library.Module import Led_Library
import time
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"we need 2 arguments but you give {len(sys.argv)-1} arguments")
    channel = sys.argv[1]
    second = sys.argv[2]
    Led_Library.set_led_pwm(channel)
    Led_Library.set_led_cycle(channel, second)
    while True:
        Led_Library.turn_on_pwm(channel)
        time.sleep(1)