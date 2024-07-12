import sys
import os
import fcntl
import struct

spi_path = "/dev/spidev{}.{}"

# fcntl spi function call
SPI_IOC_MAGIC = 'k'

def _IOR(type, nr, size):
    return (2 << 30 | (ord(type) << 8) | (nr << 0) | (size << 16))

def _IOW(type, nr, size):
    return (1 << 30 | (ord(type) << 8) | (nr << 0) | (size << 16))

SPI_IOC_RD_MODE = _IOR(SPI_IOC_MAGIC, 1, 1)
SPI_IOC_WR_MODE = _IOW(SPI_IOC_MAGIC, 1, 1)
SPI_IOC_RD_BITS_PER_WORD = _IOR(SPI_IOC_MAGIC, 3, 1)
SPI_IOC_WR_BITS_PER_WORD = _IOW(SPI_IOC_MAGIC, 3, 1)
SPI_IOC_RD_MAX_SPEED_HZ = _IOR(SPI_IOC_MAGIC, 4, 4)
SPI_IOC_WR_MAX_SPEED_HZ = _IOW(SPI_IOC_MAGIC, 4, 4)

# create spi file descriptor
def spi_open(bus, device):
    try:
        return os.open(spi_path.format(bus, device), os.O_RDWR)
    except IOError as e:
        print(f"Error : SPI Device{bus}.{device} File Open : {e}")
        sys.exit(1)


# mode : 0 ~ 3
# SPI_MODE_0: CPOL = 0, CPHA = 0
# SPI_MODE_1: CPOL = 0, CPHA = 1
# SPI_MODE_2: CPOL = 1, CPHA = 0
# SPI_MODE_3: CPOL = 1, CPHA = 1
def spi_set_mode(fd, mode):
    try:
        fcntl.ioctl(fd, SPI_IOC_WR_MODE, struct.pack('B', mode))
    except IOError as e:
        print(f"Error : SPI Device{fd} {mode} mode change : {e}")
        sys.exit(1)

# set device's max hz
def spi_set_speed(fd, hz):
    try:
        fcntl.ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, struct.pack('I', hz))
    except IOError as e:
        print(f"Error : SPI Device{fd} Max Speed Setting : {e}")
        sys.exit(1) 

# set bits per word
def spi_set_bits_per_word(fd, bits):
    try:
        fcntl.ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, struct.pack('B', bits))
    except IOError as e:
        print(f"Error : SPI Device{fd} Setting Bits per Word : {e}")
        sys.exit(1)

# read data from device
def spi_read(fd, length):
    try:
        return os.read(fd, length)
    except IOError as e:
        print(f"Error : SPI Device{fd} Reading : {e}")
        sys.exit(1)

# transfer data to device
def spi_write(fd, data):
    try:
        os.write(fd, data)
    except IOError as e:
        print(f"Error : SPI Device{fd} Writing : {e}")
        sys.exit(1)

# quit spi connect
def spi_quit(fd):
    os.close(fd)