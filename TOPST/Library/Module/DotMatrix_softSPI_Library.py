from.. import Soft_SPI_Library as spi
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

def set_spi(mosi_pin, sclk_pin, rclk_pin):
    spi.set_soft_spi(0, sclk_pin, mosi_pin, 0, rclk_pin)

def transfer_data(data, mosi_pin, sclk_pin, rclk_pin):
    send_data = []
    i = 0
    for byte in data:
        send_data.append(struct.pack('BB', rows[i], byte))
        i+=1
    for m in range(len(data)):
        spi.write_data(send_data[m],  mosi_pin, sclk_pin)
        print(send_data[m])
        spi.RClock(rclk_pin)

def clear_spi(mosi_pin, sclk_pin, rclk_pin):
    spi.clear_soft_spi(0, sclk_pin, mosi_pin, 0, rclk_pin)
