from .. import GPIO_Library as gpio

def set_device(gpio_pin):
    gpio.export(gpio_pin)
    gpio.set_direction(gpio_pin, "in")

def get_value(gpio_pin):
    value = gpio.get_value(gpio_pin)
    if value == 1:
        return True
    else:
        return False