from ..Library.Module import PCF8591_Library as pcf
from ..Library.Module import MQ2_Library as mq2
import time

bus = 1
addr = 0x48
channel = 00
auto_increment = 0
input = 0
output = 1
gpio_pin = 84

if __name__ == "__main__":
    fd = pcf.open_device(bus, addr)
    mq2.set_device(gpio_pin)
    control_byte = pcf.get_control_byte(output, input, auto_increment, channel)
    pcf.write_device(fd, control_byte)
    for i in range(10):
        print(pcf.read_device(fd, control_byte))
        print(mq2.get_value(gpio_pin))
        time.sleep(0.05)
    pcf.quit_device(fd)