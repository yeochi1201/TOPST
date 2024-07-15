from ..Library.Module import DotMatrix_softSPI_Library as dot
import sys
ss_pin = 65
sclk_pin = 86
mosi_pin = 90

data =[
    0b00011000,
    0b00011000,
    0b00000000,
    0b11000011,
    0b01100110,
    0b00111100,
    0b00011000,
    0b00000000
]

if __name__ == "__main__":
    dot.set_spi(ss_pin, mosi_pin, sclk_pin)
    while True:
        dot.transfer_data(data,mosi_pin,sclk_pin)
        if(KeyboardInterrupt):
            dot.clear_spi(ss_pin, mosi_pin, sclk_pin)
            sys.exit(1)