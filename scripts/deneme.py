#!/usr/bin/env python3

import telemetri_verileri as tv
from time import sleep

def calistir():
	while True:
		try:
			print(tv.pitch)
			sleep(0.2)
		except:
			print("hata")
