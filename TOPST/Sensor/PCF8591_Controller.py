from ..Library.Module import PCF8591_Library as pcf

bus = 1
addr = 0x48
channel = 00
auto_increment = 0
input = 0
output = 1

if __name__ == "__main__":
    fd = pcf.open_device(bus, addr)
    for i in range(10):
        control_byte = pcf.get_control_byte(output, input, auto_increment, channel)
        print(pcf.read_device(fd, control_byte))
    pcf.quit_device(fd)