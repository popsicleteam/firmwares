from cst8xx import Cst8xx
from machine import SPI, Pin
from st77xx import St7789

display = None
touch = None


def init():
    # ============================================================
    # 初始化显示与触摸
    # ============================================================
    global display, touch

    spi = SPI(1, baudrate=80_000_000, sck=Pin(38), mosi=Pin(39))
    display = St7789(spi=spi, res=(240, 240), rst=40, dc=45, cs=21, bl=46, rot=0)

    touch = Cst8xx(
        i2c_dev=1, sda=42, scl=41, rst_pin=47, irq_pin=48, width=240, height=240
    )
