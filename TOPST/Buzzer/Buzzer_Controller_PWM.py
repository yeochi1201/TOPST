from ..Library.Module import Buzzer_Library
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"we need 2 arguments but you give {len(sys.argv)-1} arguments")
    
    channel = sys.argv[1]
    hz = sys.argv[2]
    Buzzer_Library.set_buzzer_pwm(channel)
    Buzzer_Library.turn_on_pwm(channel)
    while True:
        Buzzer_Library.set_tone_pwm(channel, hz)
        if(input(hz)=="q"):
            Buzzer_Library.turn_off_pwm(channel)
        else:
            Buzzer_Library.turn_on_gpio(channel)