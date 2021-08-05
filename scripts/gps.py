#!/usr/bin/env python3

import telemetri_verileri as tv
import serial
from time import sleep

def calistir():
	with serial.Serial('/dev/ttyS0', 9600) as ser:
		while True:
			gps_verisi = ser.readline().strip().decode()
			if gps_verisi[:6] == "$GNRMC":
				gps = s.split(",")
				tv.saat, tv.dakika, tv.saniye = int(x[1][:2]) + 3, x[1][2:4], x[1][4:6]
				tv.gun, tv.ay, tv.yil = x[9][:2], x[9][2:4], x[9][4:6] + 2000
				tv.gps_latitude = float(x[3][:2]) + float(x[3][2:]) / 60
				tv.gps_longitude = float(x[6][:3]) + float(x[6][3:]) / 60
