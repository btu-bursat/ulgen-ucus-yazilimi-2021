#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import telemetri

def logla(mesaj):
	try:
		f = open("/home/pi/ulgen/log.txt", "a")
		f.write("{}, {}: {}\n".format(telemetri.zaman_damgasi(), tv.paket_numarasi, mesaj))
	except:
		return
