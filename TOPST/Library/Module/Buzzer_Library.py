from .. import GPIO_Library
from .. import PWM_Library

#GPIO Buzzer
# Set buzzer gpio
def set_buzzer_gpio(gpio_pin):
    GPIO_Library.export(gpio_pin)
    GPIO_Library.set_direction(gpio_pin, "out")

# Quit buzzer gpio
def quit_buzzer_gpio(gpio_pin):
    GPIO_Library.unexport(gpio_pin)

def turn_on_gpio(gpio_pin):
    GPIO_Library.set_value(gpio_pin , 1)

def turn_off_gpio(gpio_pin):
    GPIO_Library.set_value(gpio_pin , 0)

#PWM Buzzer
def set_buzzer_pwm(channel):
    PWM_Library.export(channel)

def quit_buzzer_pwm(channel):
    PWM_Library.unexport(channel)

def set_tone_pwm(channel, hz):
    PWM_Library.set_period_sec(channel, hz)
    PWM_Library.set_cycle_sec(channel, hz)    

def turn_on_pwm(channel):
    PWM_Library.set_enable(channel, 1)

def turn_off_pwm(channel):
    PWM_Library.set_enable(channel, 0)