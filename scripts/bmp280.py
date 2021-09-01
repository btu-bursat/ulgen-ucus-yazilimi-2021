#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import board
import adafruit_bmp280
from time import sleep

def calistir():
	i2c = board.I2C()
	bmp180 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

	# Sicaklik, basinc ve yukseklik verisi yarim saniyede bir guncellenir
	while True:
		# Basinci ucusa baslama noktasina gore ayarlanir ve yukseklik dogru olculur
		bmp180.sea_level_pressure = float(tv.sifir_noktasi)
		tv.sicaklik = bmp180.temperature
		tv.basinc = bmp180.pressure
		tv.yukseklik = bmp180.altitude
		sleep(0.5)
