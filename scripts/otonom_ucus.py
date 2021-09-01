#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
from time import sleep

def calistir():
	return
	# Ivme sensorundeki sifir degeri
	ivme_sifir_degeri = 1.545
	while True:
		if tv.uydu_statusu == "1":
			if tv.ivme_z < ivme_sifir_degeri and tv.yukseklik >= 400:
				tv.uydu_statusu = "2"
		elif tv.uydu_statusu == "2":
			if tv.ivme_z < ivme_sifir_degeri and tv.yukseklik < 400:
				tv.uydu_statusu = "3"
		elif tv.uydu_statusu == "3":
			if tv.ivme_z < ivme_sifir_degeri and tv.yukseklik == 200:
				tv.uydu_statusu = "4"
		elif tv.uydu_statusu == "4":
			if tv.ivme_z < ivme_sifir_degeri and tv.yukseklik < 200:
				tv.uydu_statusu = "5"
		elif tv.uydu_statusu == "5":
			if tv.ivme_z == ivme_sifir_degeri and tv.yukseklik == 0:
				tv.uydu_statusu = "6"
		sleep(0.3)
