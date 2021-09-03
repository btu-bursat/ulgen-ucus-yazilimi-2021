#!/usr/bin/env python3
# Ulgen, 2021

from time import sleep

import telemetri_verileri as tv

def calistir():
	onceki_yukseklik = tv.yukseklik
	sure = 1

	# Yukseklik degisimine gore hiz hesaplanir
	while True:
		yukseklik_degisimi = float(tv.yukseklik) - float(onceki_yukseklik)
		tv.inis_hizi = yukseklik_degisimi / sure
		onceki_yukseklik = tv.yukseklik
		sleep(sure)
