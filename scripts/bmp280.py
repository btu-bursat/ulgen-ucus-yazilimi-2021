#!/usr/bin/env python3
# Ulgen, 2021

import board
import adafruit_bmp280
from time import sleep

import telemetri_verileri as tv

def calistir():
	i2c = board.I2C()
	bmp180 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

	while True:
		# Yuksekligin dogru hesaplanabilmesi icin basinc ucusa baslangic
		# noktasindaki degere gore olculur
		bmp180.sea_level_pressure = float(tv.sifir_noktasi)
		tv.sicaklik = bmp180.temperature
		tv.basinc = bmp180.pressure
		tv.yukseklik = bmp180.altitude
		sleep(0.5)
