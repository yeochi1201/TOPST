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
    time_start = time.time()
    gpio.set_direction(gpio_pin, "in")
    print(f"trigger time : {time_start-time.time()}")

def get_data(gpio_pin):
    time_start = time.time()
    data = [0 for i in range(5)]
    counter = 0
    prev_state = 1
    idx = 0
    print(f"defnition time : {time_start-time.time()}")
    for i in range(85):
        time_start = time.time()
        while(gpio.get_value(gpio_pin) == prev_state):
            counter += 1
            time.sleep(0.000001)
            if counter == 255:
                print("Error")
                break
        
        prev_state = gpio.get_value(gpio_pin)
        if counter == 255:
            break
        print(f"get value time : {time_start-time.time()}")
        time_start = time.time()
        if i >= 4 and i%2==0:
            data[idx//8] <<= 1
            if counter > 16:
                data[idx//8] |= 1
            idx += 1
        print(f"record value time : {time_start - time.time()}")
    return data