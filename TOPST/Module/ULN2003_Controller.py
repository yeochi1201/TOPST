from ..Library.Module import ULN2003_Library as uln
pins = [112, 113, 114, 121]

step_count = 4096
step_sleep = 0.002
direction = True
if __name__ == "__main__":
    uln.set_driver(pins)
    uln.rotation(step_count, direction)