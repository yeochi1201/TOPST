from ..Library.Module import Led_Library
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"we need 2 arguments but you give {len(sys.argv)-1} arguments")
    gpio_pin = sys.argv[1]
    second = sys.argv[2]
    Led_Library.set_led_gpio(gpio_pin)
    while True:
        Led_Library.turn_on_gpio(gpio_pin)
        time.sleep(int(second))
        Led_Library.turn_off_gpio(gpio_pin)
        time.sleep(int(second))
        if(KeyboardInterrupt):
            Led_Library.quit_led_gpio(gpio_pin)
            break