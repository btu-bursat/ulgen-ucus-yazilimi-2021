#!/usr/bin/env python3

import telemetri_verileri as tv
import serial
from time import sleep

def calistir():
	with serial.Serial('/dev/ttyS0', 9600) as ser:
		while True:
			#gps_verisi = ser.readline().strip().decode()
			sleep(1)
