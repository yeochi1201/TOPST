from ..Library.Module import PCF8591_Library as pcf

def getVector(fd, x_byte, y_byte):
    x = pcf.read_device(fd, x_byte)
    y = pcf.read_device(fd,y_byte)
    return x, y

if __name__ == "__main__":
    x, y = 0, 0
    fd = pcf.open_device(1)
    axisy = pcf.get_control_byte(1,0,0,0)
    axisx = pcf.get_control_byte(0,0,0,1)
    while(True):
        x , y = getVector(fd, axisx, axisy)
        print(f"X : {x} | Y : {y}")