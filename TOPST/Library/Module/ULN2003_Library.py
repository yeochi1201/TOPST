from .. import GPIO_Library as gpio

pins= []
def set_driver(input_pins):
    for pin in input_pins:
        gpio.export(pin)
        gpio.set_direction(pin, "out")
        gpio.set_value(pin, 0)
        pins.append(pin)

def set_location(input_pin, input_pin2 = -1):
    for pin in pins:
        if(pin == input_pin):
            gpio.set_value(pin, 1)
        elif(input_pin2 != -1 and pin == input_pin2):
            gpio.set_value(pin, 1)
        else:
            gpio.set_value(pin, 0)