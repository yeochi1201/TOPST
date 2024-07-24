from .. import Soft_SPI_Library as spi

def set_spi(mosi_pin, sclk_pin, rclk_pin):
    spi.set_soft_spi(0, mosi_pin, 0, sclk_pin, rclk_pin)

def transfer_data(data, mosi_pin, sclk_pin):
    spi.write_data(data,  mosi_pin, sclk_pin)

def clear_spi(mosi_pin, sclk_pin, rclk_pin):
    spi.clear_soft_spi(0, mosi_pin,0,sclk_pin, rclk_pin)