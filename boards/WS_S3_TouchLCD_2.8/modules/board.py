from cst3xx import Cst3xx
from machine import SPI, Pin
from st77xx import St7789

display = None
touch = None


def init():
    # ============================================================
    # 初始化显示与触摸
    # ============================================================
    global display, touch

    spi = SPI(1, baudrate=80_000_000, sck=Pin(40), mosi=Pin(45), miso=Pin(46))
    display = St7789(spi=spi, res=(240, 320), rst=39, dc=41, cs=42, bl=5, rot=0)

    touch = Cst3xx(i2c_dev=1, sda=1, scl=3, rst_pin=2, irq_pin=4, width=240, height=320)
