#!/usr/bin/env python3

import sensor_verileri as sv
from time import sleep

def calistir():
	onceki_yukseklik = sv.yukseklik
	olcekleme_zamani = 1
	sifir_noktasi = sv.sifir_noktasi
	while True:
		yukseklik_degisimi = sv.yukseklik - onceki_yukseklik
		sv.inis_hizi = yukseklik_degisimi / olcekleme_zamani
		sleep(olcekleme_zamani)
