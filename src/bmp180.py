#!/usr/bin/env python3

import sensor_verileri as sv
import board
import adafruit_bmp280
from time import sleep

def calistir():
	i2c = board.I2C()
	bmp180 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
	bmp180.sea_level_pressure = 1013.25
	while True:
		sv.sicaklik = bmp180.temperature
		sv.basinc = bmp180.pressure
		sv.yukseklik = bmp180.altitude
		sleep(2)
