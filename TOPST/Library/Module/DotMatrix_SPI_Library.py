from .. import SPI_Library
from .. import GPIO_Library
import struct
import time

rows = [
    0x01,
    0x02,
    0x03,
    0x04,
    0x05,
    0x06,
    0x07,
    0x00,
]

def set_spi(bus, device, gpio_pin):
    fd = SPI_Library.spi_open(bus, device)
    SPI_Library.spi_set_bits_per_word(fd, 8)
    SPI_Library.spi_set_speed(fd, 10000)
    SPI_Library.spi_set_mode(fd, 0)
    GPIO_Library.export(gpio_pin)
    GPIO_Library.set_direction(gpio_pin, "out")
    clear_matrix(fd, gpio_pin)
    return fd

# message = 8byte array
def transfer_msg(fd, row, message, pin):
    data = struct.pack('BB', rows[row], message)
    SPI_Library.spi_write(fd, data)
    output_data(pin)

def output_data(pin):   
    GPIO_Library.set_value(pin, 1)
    time.sleep(0.1)
    GPIO_Library.set_value(pin, 0)
    time.sleep(0.1)

off = 0b11111111
def clear_matrix(fd, pin):
    for row in range(0, 8):
        SPI_Library.spi_write(fd, struct.pack('BB', rows[row], off))
        output_data(pin)

def quit_spi(fd):
    SPI_Library.spi_quit(fd)