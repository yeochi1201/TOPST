from .. import GPIO_Library

def set_ball_tilt_sensor(gpio_pin):
    GPIO_Library.export(gpio_pin)
    GPIO_Library.set_direction(gpio_pin, "in")
    GPIO_Library.set_edge(gpio_pin, "both")

def get_sensor_value(gpio_pin):
    return GPIO_Library.get_value(gpio_pin)

def quit_ball_tile_sensor(gpio_pin):
    GPIO_Library.unexport(gpio_pin)