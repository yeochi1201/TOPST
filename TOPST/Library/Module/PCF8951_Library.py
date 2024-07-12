from .. import I2C_Library as i2c
from .. import GPIO_Library as gpio

# using fcntl
# icotl slave value
slave= 0x0703
addr= 0x48
data_len = 8
pin_map = [0x00, 0x01, 0x02, 0x03, 0x04]
def open_device(bus):
    fd =  i2c.i2c_open(bus)
    i2c.i2c_set_slave(bus, addr, slave)
    return fd

def write_device(fd, gpio_pin, data):
    i2c.i2c_write(fd, pin_map[gpio_pin], data)

def read_device(fd, gpio_pin):
    return i2c.i2c_read(fd, pin_map[gpio_pin], data_len)

# using sysfs
def open_path(bus):
    return i2c.i2c_sysfs_path(bus, 0x20)

def read_path(sys_path, gpio_pin):
    file_path = f"gpio{gpio_pin}/value"
    return i2c.read_sysfs_file(sys_path, file_path)

def write_path(sys_path, gpio_pin, data):
    file_path = f"gpio{gpio_pin}/value"
    i2c.write_sysfs_file(sys_path, file_path,str(data))