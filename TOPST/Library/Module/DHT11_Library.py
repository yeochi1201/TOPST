from .. import GPIO_Library as gpio
import time

def set_device(gpio_pin):
    gpio.export(gpio_pin)
    gpio.set_direction(gpio_pin, "in")

def read_value(gpio_pin):
    trigger(gpio_pin)
    return get_data(gpio_pin)

def trigger(gpio_pin):
    gpio.set_direction(gpio_pin, "out")
    gpio.set_value(gpio_pin, 0)
    time.sleep(0.018)
    gpio.set_direction(gpio_pin, "in")

def get_data(gpio_pin):
    data = [0 for i in range(5)]
    counter = 0
    prev_state = 1
    idx = 0
    for i in range(85):
        while(gpio.get_value(gpio_pin)== prev_state):
            counter += 1
            time.sleep(0.000001)
            if counter == 255:
                break
        prev_state = gpio.get_value(gpio_pin)
        if counter == 255:
            break
        if i >= 4 and i%2==0:
            data[idx/8] <<= 1
            if counter > 16:
                data[idx/8] |= 1
            j += 1
    return data