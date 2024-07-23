from ..Library.Module import DHT11_Library as dht

if __name__ == "__main__":
    gpio_pin = 83

    dht.set_device(83)
    while(True):
        print (dht.read_value(83))