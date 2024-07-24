import time
import sys
import os

export_path = "/sys/class/gpio/export"
unexport_path = "/sys/class/gpio/unexport"
gpio_path_base = "/sys/class/gpio/gpio{}/"
direction_path_base = "/sys/class/gpio/gpio{}/direction"
value_path_base = "/sys/class/gpio/gpio{}/value"
edge_path_base = "/sys/class/gpio/gpio{}/edge"

in_bytes = b'in'
out_bytes = b'out'

def export(gpio_pin):
    try:
          with open(export_path, 'w') as export_file:
            export_file.write(str(gpio_pin))
    except IOError as e:
        print(f"Error : GPIO {gpio_pin} Exporting : {e}")
        sys.exit(1)

def unexport(gpio_pin):
    try:
          with open(unexport_path, 'w') as unexport_file:
            unexport_file.write(str(gpio_pin))
    except IOError as e:
        print(f"Error : GPIO {gpio_pin} Unxporting : {e}")
        sys.exit(1)

def get_file(gpio_pin):
    try:
        direction_file = os.open(direction_path_base.format(gpio_pin), os.O_WRONLY)
        value_file = os.open(value_path_base.format(gpio_pin), os.O_RDWR)
        return direction_file, value_file
    except IOError as e:
        print(f"Error: get file descriptor {e}") 
        sys.exit(1)

def set_direction(fd, direction):
        try:
            os.write(fd, direction)
        except IOError as e:
            print(f"Error : GPIO {fd} direction : {e}")
            sys.exit(1)

# value : 1, 0
def set_value(fd, value):
        try:
            os.write(fd, value)
        except IOError as e:
            print(f"Error : GPIO {fd} set value : {e}")
            sys.exit(1)

# only on 'in' direction
def get_value(fd):
        try:
            return os.read(fd, 1)[0]
        except IOError as e:
            print(f"Error : GPIO {fd} get value : {e}")
            sys.exit(1)


data = [0 for i in range(5)]
counter = 0
prev_state = 1
idx = 0
direction_fd = None
value_fd = None

def set_device(gpio_pin):
    global direction_fd
    global value_fd
    export(gpio_pin)
    print("export complete")
    direction_fd, value_fd = get_file(gpio_pin)
    print(direction_fd, value_fd)
    set_direction(direction_fd, in_bytes)

def read_value():
    trigger()
    print("start")
    return get_data()

def trigger():
    set_direction(direction_fd, out_bytes)
    set_value(value_fd, 0)
    time.sleep(0.018)
    set_value(value_fd, 1)
    time_start = time.time()
    set_direction(direction_fd, in_bytes)
    print(f"trigger time : {time_start-time.time()}")

def get_data():
    time_start = time.time()
    global data
    global counter
    global prev_state
    global idx
    print(f"definition time : {time_start-time.time()}")
    for i in range(85):
        while(get_value(value_fd) == prev_state):
            time_start = time.time()
            counter += 1
            if counter == 255:
                print("Error")
                break
            print(f"get value time : {time_start-time.time()}")
        prev_state = get_value(value_fd)
        if counter == 255:
            break
        
        time_start = time.time()
        if i >= 4 and i%2==0:
            data[idx//8] <<= 1
            if counter > 3:
                data[idx//8] |= 1
            idx += 1
        print(f"record value time : {time_start - time.time()}")
    return data

def quit_device(gpio_pin):
    unexport(gpio_pin)
    os.close(direction_fd)
    os.close(value_fd)