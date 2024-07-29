from ..Library import GPIO_Library as GPIO
import time

def set_soft_spi(ss_pin = 0, sclk_pin = 0, mosi_pin = 0, miso_pin = 0, rclk_pin = 0):
    if(ss_pin):
        GPIO.export(ss_pin)
        GPIO.set_direction(ss_pin, "out")
        GPIO.set_value(ss_pin, 0)
    if(rclk_pin):
        GPIO.export(rclk_pin)
        GPIO.set_direction(rclk_pin, "out")
        GPIO.set_value(rclk_pin, 0)
    if(mosi_pin):
        GPIO.export(mosi_pin)
        GPIO.set_direction(mosi_pin, "out")
    if(miso_pin):
        GPIO.export(miso_pin)
        GPIO.set_direction(miso_pin, "in")
    if(sclk_pin):
        GPIO.export(sclk_pin)
        GPIO.set_direction(sclk_pin, "out")
        GPIO.set_value(sclk_pin, 1)

def clear_soft_spi(ss_pin = 0,sclk_pin = 0, mosi_pin = 0, miso_pin = 0, rclk_pin = 0):
    if(ss_pin):
        GPIO.unexport(ss_pin)
    if(sclk_pin):
        GPIO.unexport(sclk_pin)
    if(mosi_pin):
        GPIO.unexport(mosi_pin)
    if(miso_pin):
        GPIO.unexport(miso_pin)
    if(rclk_pin):
        GPIO.unexport(rclk_pin)

def RClock(rclk_pin):
    GPIO.set_value(rclk_pin, 0)
    time.sleep(0.002)
    GPIO.set_value(rclk_pin, 1)
    time.sleep(0.002)

def duflex_SPI(data, mosi_pin, miso_pin, rclk_pin):
    response = []
    for byte in data:
        response_byte = duflex_byte(byte, mosi_pin, miso_pin, rclk_pin)
        response.append(response_byte)
    return response

def duflex_byte(byte, sclk_pin, mosi_pin, miso_pin):
    response_byte = []
    for i in range(8):
        bit = (byte >> (7-i)) & 0x01
        GPIO.set_value(mosi_pin, bit)

        GPIO.set_value(sclk_pin, 1)
        time.sleep(0.0001)

        response_bit = GPIO.get_value(miso_pin)
        response_byte = (response_byte << 1) | response_bit

        GPIO.set_value(sclk_pin, 0)
        time.sleep(0.0001)

    return response_byte

def write_data(data, rclk_pin, mosi_pin,sclk_pin):
    GPIO.set_value(rclk_pin, 0)
    for byte in data:
        write_byte(byte,sclk_pin, mosi_pin)
    RClock(rclk_pin)
def write_byte(byte, sclk_pin, mosi_pin):
    writed = []
    GPIO.set_value(sclk_pin , 0)
    for i in range (8):
        bit = (byte << i) & 0x80
        GPIO.set_value(mosi_pin , bit)
        writed.append(bit)
        #toggle
        GPIO.set_value(sclk_pin, 1)
        time.sleep(0.002)
        GPIO.set_value(sclk_pin, 0)
        time.sleep(0.002)
    print(writed)

def read_data(length, miso_pin, rclk_pin):
    response = []
    for i in range(length):
        response_byte = read_byte(miso_pin, rclk_pin)
        response.append(response_byte)

    return response

def read_byte(miso_pin, rclk_pin):
    response_byte = []
    GPIO.set_value(rclk_pin, 1)
    for i in range(8):
        response_bit = GPIO.get_value(miso_pin)
        response_byte = (response_byte << 1) | response_bit

        GPIO.set_value(rclk_pin , 0)
        GPIO.set_value(rclk_pin, 1)

    return response_byte
