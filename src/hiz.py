#!/usr/bin/env python3

import telemetri_verileri as tv
from time import sleep

def calistir():
	onceki_yukseklik = tv.yukseklik
	olcekleme_zamani = 1
	while True:
		yukseklik_degisimi = tv.yukseklik - onceki_yukseklik
		tv.inis_hizi = yukseklik_degisimi / olcekleme_zamani
		onceki_yukseklik = tv.yukseklik
		sleep(olcekleme_zamani)
