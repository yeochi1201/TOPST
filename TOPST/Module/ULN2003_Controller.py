from ..Library.Module import ULN2003_Library as uln
import time

pins = [112, 113, 114, 121]

if __name__ == "__main__":
    uln.set_driver(pins)
    i = 0
    while(True):
        for i in range(0,8):
            if i%2 ==0:
                uln.set_location(pins[i/2])
            else:
                uln.set_location(pins[i/2],pins[(i/2+1)%4])
            time.sleep(1)