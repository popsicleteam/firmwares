import time

import camera
from machine import Pin


def init(**kwargs):
    pwr_en = Pin(18, Pin.OUT, value=0)

    time.sleep_ms(500)

    camera.init(
        framesize=camera.FRAME_QVGA,
        d0=3,
        d1=42,
        d2=46,
        d3=48,
        d4=4,
        d5=17,
        d6=11,
        d7=13,
        vsync=10,
        href=14,
        pclk=40,
        xclk=21,
        sda=12,
        scl=9,
        **kwargs,
    )


def deinit():
    camera.deinit()
