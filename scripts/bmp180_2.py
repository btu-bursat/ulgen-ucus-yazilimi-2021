#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import board
import Adafruit_BMP.BMP085 as BMP085
from time import sleep

def calistir():
	sensor = BMP085.BMP085()
	while True:
		tv.sicaklik = sensor.read_temperature()
		tv.basinc = sensor.read_pressure()
		tv.yukseklik = sensor.read_altitude()
		sleep(0.5)
