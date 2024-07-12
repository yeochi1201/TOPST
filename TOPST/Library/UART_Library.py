import sys
import os

uart_path = "/dev/tty{}"

def uart_set(channel, bps):
    try:
        os.system(f"stty -F {uart_path.format(channel)} {bps}")
        return os.open(uart_path.format(channel), os.O_RDWR | os.O_NOCTTY)
    except IOError as e:
        print(f"Error : Uart {channel} Opening & Setting : {e}")

def uart_quit(fd):
    os.close(fd)

def uart_read(fd, length):
    try:
        return os.read(fd, length)
    except IOError as e:
        print(f"Error : Uart {fd} Reading : {e}")
        sys.exit(1)

def uart_write(fd, data):
    try:
        os.write(fd, data)
    except IOError as e:
        print(f"Error : Uart {fd} Writing : {e}")
        sys.exit(1) 