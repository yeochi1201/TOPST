from .. import Soft_SPI_Library as spi
import struct
rows = [
    0x00,
    0x01,
    0x02,
    0x03,
    0x04,
    0x05,
    0x06,
    0x07
]


def set_spi(ss_pin, mosi_pin, sclk_pin):
    spi.set_soft_spi(ss_pin, mosi_pin, 0, sclk_pin)

def transfer_data(data, ss_pin, mosi_pin, sclk_pin):
    send_data = []
    i = 0
    for byte in data:
        send_data.append(struct.pack('BB', rows[i], byte))
        i+=1
    for i in range(len(data)):
        spi.write_data(send_data[i], mosi_pin, sclk_pin)
        spi.RClock(ss_pin)

def clear_spi(ss_pin, mosi_pin, sclk_pin):
    spi.clear_soft_spi(ss_pin, mosi_pin,0,sclk_pin)