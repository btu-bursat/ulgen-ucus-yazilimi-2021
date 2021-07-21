#!/usr/bin/env python3

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
			tv.paket_numarasi = 0
			tv.uydu_statusu = 1
			tv.komut = "0"
		elif tv.komut == "2":
			motor.tasiyiciyi_ayir()
		elif tv.komut == "3":
			motor.motor_calistir()
		elif tv.komut == "4":
			motor.motor_durdur()
		sleep(1)
