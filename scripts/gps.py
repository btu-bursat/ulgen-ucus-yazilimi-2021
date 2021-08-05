#!/usr/bin/env python3

import telemetri_verileri as tv
import serial
from time import sleep

def calistir():
	with serial.Serial('/dev/ttyS0', 9600) as ser:
		while True:
			gps_verisi = ser.readline().strip().decode()
			if gps_verisi[:6] == "$GNRMC":
				gps = gps_verisi.split(",")
				if gps[1] != "":
					tv.saat, tv.dakika, tv.saniye = int(gps[1][:2]) + 3, gps[1][2:4], gps[1][4:6]
				if gps[9] != "":
					tv.gun, tv.ay, tv.yil = gps[9][:2], gps[9][2:4], int(gps[9][4:6]) + 2000
				if gps[3] != "":
					tv.gps_latitude = float(gps[3][:2]) + float(gps[3][2:]) / 60
				if gps[6] != "":
					tv.gps_longitude = float(gps[6][:3]) + float(gps[6][3:]) / 60
