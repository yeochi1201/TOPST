from ..Library.Module import DotMatrix_SPI_Library as dot
import sys

# transfer data
message = [
    0b11100111,
    0b11100111,
    0b11100111,
    0b00000000,
    0b00000000,
    0b11100111,
    0b11100111,
    0b11100111,
]

latch = 84 

if __name__ == "__main__":
    # setting dot matrix
    fd = dot.set_spi(0,0, latch)
    #transfer data to dot matrix
    
    # exit program when keyboard interrupt
    while True:
        for row, data in enumerate(message):
            dot.transfer_msg(fd ,row, data, latch)
            print(row)
        if(KeyboardInterrupt):
            dot.quit_spi(fd)
            sys.exit(1)