#!/usr/bin/env python3

import telemetri_verileri as tv
import board
import adafruit_bmp280
from time import sleep

def calistir():
	i2c = board.I2C()
	bmp180 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
	#bmp180.sea_level_pressure = 1013.25
	while True:
		bmp180.sea_level_pressure = tv.sifir_noktasi
		tv.sicaklik = bmp180.temperature
		tv.basinc = bmp180.pressure
		tv.yukseklik = bmp180.altitude
		sleep(0.5)
