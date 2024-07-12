from ..Library.Module import Buzzer_Library
import time
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"we need 2 arguments but you give {len(sys.argv)-1} arguments")
    
    gpio_pin = sys.argv[1]
    second = sys.argv[2]

    Buzzer_Library.set_buzzer_gpio(gpio_pin)
    
    while True:
        Buzzer_Library.turn_on_gpio(gpio_pin)
        time.sleep(second)
        Buzzer_Library.turn_off_gpio(gpio_pin)
        time.sleep(second)