from .. import Soft_SPI_Library as spi
import struct

rows = [
    0xFE,
    0xFD,
    0xFB,
    0xF7, 
    0xEF,
    0xDF,
    0xBF,
    0x7F
]

def set_spi(ss_pin, mosi_pin, sclk_pin):
    spi.set_soft_spi(ss_pin, mosi_pin, 0, sclk_pin)

def transfer_data(data, ss_pin, mosi_pin, sclk_pin):
    send_data = []
    i = 0
    for byte in data:
        send_data.append(struct.pack('BB', byte, rows[i]))
        i+=1
    for m in range(len(data)):
        spi.write_data(send_data[m], ss_pin, mosi_pin, sclk_pin)
        print(send_data[m])


def clear_spi(ss_pin, mosi_pin, sclk_pin):
    spi.clear_soft_spi(ss_pin, mosi_pin,0,sclk_pin)