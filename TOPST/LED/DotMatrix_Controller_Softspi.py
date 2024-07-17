from ..Library.Module import DotMatrix_softSPI_Library as dot
import sys
rclk_pin = 90 # RCLK
sclk_pin = 86 # SRCLK
mosi_pin = 65 # MOSI
'''
data =[
    0b00011000, #18
    0b00011000, #18
    0b00000000, #00
    0b11000011, #c3
    0b01100110, #66
    0b00111100, #3C
    0b00011000, #18
    0b00000000  #00
]
'''
data =[

    0b00001111,  #00
    0b11110000,  #00
    0b00001111,  #00
    0b11110000,  #00
    0b00001111,  #00
    0b11110000,  #00
    0b00001111,  #00
    0b11110000  #00
]

if __name__ == "__main__":
    dot.set_spi(mosi_pin, sclk_pin, rclk_pin)
    while True:
        dot.transfer_data(data, mosi_pin,sclk_pin, rclk_pin)
