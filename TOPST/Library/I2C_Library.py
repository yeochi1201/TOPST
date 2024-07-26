import os
import sys
import fcntl

device_path = "/dev/i2c-{}"
i2c_slave = 0x0703

# fcntl
def i2c_open(bus):
    try:
        fd = os.open(device_path.format(bus), os.O_RDWR)
    except FileNotFoundError:
        print(f"Error : i2c_open : i2c device file not found")
        sys.exit(1)
    return fd

def i2c_set_slave(fd, addr):
    try:
        fcntl.ioctl(fd, i2c_slave, addr)
    except IOError as e:
        print(f"Error : Setting I2C Address {addr}: {e}")
        sys.exit(1)

def i2c_read_reg(fd, reg, length):
    try:
        i2c_write(fd, reg)
        return os.read(fd, length)
    except IOError as e:
        print(f"Error : I2C Device Reading Register {reg} : {e}")
        sys.exit(1)

def i2c_read(fd, length):
    try:
        return os.read(fd, length)
    except IOError as e:
        print(f"Error : I2C Device Reading Register : {e}")
        sys.exit(1)
    
def i2c_write_reg(fd, reg, data):
    try:
        os.write(fd, bytes([reg]+data))
    except IOError as e:
        print(f"Error : I2C Device Writing Register {reg} : {e}")
        sys.exit(1)

def i2c_write(fd, data):
    try:
        os.write(fd, bytes([data]))
    except IOError as e:
        print(f"Error : I2C Device Writing Register : {e}") 
        sys.exit(1)

def i2c_quit(fd):
    os.close(fd)

# file system
def i2c_sysfs_path(bus, address):
    return f"/sys/class/i2c-adapter/i2c-{bus}/{bus}-00{address:02x}/"

def read_sysfs_file(sysfs_path, file_path):
    try:
        with open(os.path.join(sysfs_path, file_path), 'r') as read_file:
            return read_file.read().strip()
    except IOError as e:
        print(f"Error : Reading sysfs_path {sysfs_path}, file_path {file_path} : {e}")
        sys.exit(1)

def write_sysfs_file(sysfs_path, file_path, data):
    try:
        with open(os.path.join(sysfs_path, file_path), 'w') as write_file:
            write_file.write(data)
    except IOError as e:
        print(f"Error : Writing Sysfs_path {sysfs_path}, file_path {file_path} : {e}")
        sys.exit(1)