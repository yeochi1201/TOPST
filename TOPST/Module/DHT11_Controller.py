from ..Library.Module import DHT11_Library as dht

if __name__ == "__main__":
    gpio_pin = 83

    dht.set_device(83)
    print (dht.read_value())
    dht.quit_device(83)