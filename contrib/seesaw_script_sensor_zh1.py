#!/usr/bin/env python


from pathlib import Path
import re

import sys

# # Dirty hack to include someone his code... to lazy to make it myself :)
# # https://github.com/AtlasScientific/Raspberry-Pi-sample-code
# sys.path.insert(0, Path("../3rdparty/adafruit_seesaw").resolve())

from adafruit_seesaw.seesaw import Seesaw

from adafruit_blinka.board.raspberrypi.raspi_4b import *
from adafruit_bus_device.i2c_device import I2CDevice, I2C

_I2C_BUS = 24
_I2C_ADDR = 0X36
_I2C_SDA_PIN = 3
_I2C_SCL_PIN = 5

_MIN_VAL = 350
_MAX_VAL = 615

i2c = I2C(SCL, SDA)

ss = Seesaw(i2c, _I2C_ADDR)

touch = ss.moisture_read()
print(touch)
# if (touch > _MAX_VAL): touch = _MAX_VAL
# if (touch < _MIN_VAL): touch = _MIN_VAL

# range = _MAX_VAL - _MIN_VAL
# pct = (touch - _MIN_VAL) / range * 100

# print(pct)
