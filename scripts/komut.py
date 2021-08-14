#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import motor
from time import sleep

def calistir():
	while True:
		# 1: kalibre etme komutu
		# 2: tasiyiciyi ayir
		# 3: motorlari calistir
		# 4: motorlari durdur
		# 5: video aktarimi -> wifi.py icinde gerceklesecek
		if tv.komut == "1":
			tv.sifir_noktasi = tv.basinc
			tv.paket_numarasi = 1
			tv.uydu_statusu = 1
