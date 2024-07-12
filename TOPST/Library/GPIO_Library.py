import os
import sys

export_path = "/sys/class/gpio/export"
unexport_path = "/sys/class/gpio/unexport"
gpio_path_base = "/sys/class/gpio/gpio{}/"
direction_path_base = "/sys/class/gpio/gpio{}/direction"
value_path_base = "/sys/class/gpio/gpio{}/value"
edge_path_base = "/sys/class/gpio/gpio{}/edge"

def is_exported(gpio_pin):
    return os.path.exists(gpio_path_base.format(gpio_pin))

def export(gpio_pin):
    if (not is_exported(gpio_pin)):
        try:
            with open(export_path, 'w') as export_file:
                export_file.write(str(gpio_pin))
        except IOError as e:
            print(f"Error : GPIO {gpio_pin} Exporting : {e}")
            sys.exit(1)

def unexport(gpio_pin):
    if (is_exported(gpio_pin)):   
        try:
            with open(unexport_path, 'w') as unexport_file:
                unexport_file.write(str(gpio_pin))
        except IOError as e:
            print(f"Error : GPIO {gpio_pin} Unexporting : {e}")
            sys.exit(1)

    # direction : in, out
def set_direction(gpio_pin, direction):
    if (is_exported(gpio_pin)):
        try:
            with open(direction_path_base.format(gpio_pin), 'w') as direction_file:
                direction_file.write(direction)
        except IOError as e:
            print(f"Error:GPIO {gpio_pin} Set Direction : {e}")
            sys.exit(1)

# value : 1, 0
def set_value(gpio_pin, value):
    if (is_exported(gpio_pin)):
        try:
            with open(value_path_base.format(gpio_pin), 'w') as value_file:
                value_file.write(str(value))
        except IOError as e:
            print(f"Error:GPIO {gpio_pin} Set Value : {e}")
            sys.exit(1)

# only on 'in' direction
def get_value(gpio_pin):
    if (is_exported(gpio_pin)):
        try:
            with open(value_path_base.format(gpio_pin), 'r') as value_file:
                return value_file.read()
        except IOError as e:
            print(f"Error:GPIO {gpio_pin} Set Value : {e}")
            sys.exit(1)

# edge : none, rising, falling, both
def set_edge(gpio_pin, edge):
    if (is_exported(gpio_pin)):
        try:
            with open(edge_path_base.format(gpio_pin), 'w') as edge_file:
                edge_file.write(edge)
        except IOError as e:
            print(f"Error:GPIO {gpio_pin} Set Edge : {e}")
            sys.exit(1)