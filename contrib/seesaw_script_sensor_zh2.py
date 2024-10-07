#!/usr/bin/env python


from pathlib import Path
import re
import statistics
import time

import sys

# adafruit_seesaw module is copied into the contrib folder
from adafruit_seesaw.seesaw import Seesaw

from adafruit_blinka.board.raspberrypi.raspi_4b import *
from adafruit_bus_device.i2c_device import I2CDevice, I2C


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def get_sensor_value(device, count):
    values=[]
    for i in range(count-1):
        values.append(device.moisture_read())
        time.sleep(1)
    return (statistics.mean(values))


_I2C_BUS = 24
_I2C_ADDR = 0X37
_I2C_SDA_PIN = 3
_I2C_SCL_PIN = 5

_MIN_VAL = 360
_MAX_VAL = 612

i2c = I2C(SCL, SDA)

ss = Seesaw(i2c, _I2C_ADDR)

result = get_sensor_value(ss, 3)

print(result)
# if (touch > _MAX_VAL): touch = _MAX_VAL
# if (touch < _MIN_VAL): touch = _MIN_VAL

# range = _MAX_VAL - _MIN_VAL
# pct = (touch - _MIN_VAL) / range * 100

# print(pct)
