#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
from time import sleep

def calistir():
	onceki_yukseklik = tv.yukseklik
	sure = 1
	while True:
		# Yukseklik degisimine gore hiz hesaplanir
		yukseklik_degisimi = float(tv.yukseklik) - float(onceki_yukseklik)
		tv.inis_hizi = yukseklik_degisimi / sure
		onceki_yukseklik = tv.yukseklik
		sleep(sure)
