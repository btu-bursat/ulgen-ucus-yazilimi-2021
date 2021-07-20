#!/usr/bin/env python3

import telemetri_verileri as tv
from time import sleep

def calistir():
	while True:
		# 1: kalibre etme komutu
		# 2: tasiyiciyi ayir
		# 3: motorlari calistir
		# 4: motorlari durdur
		# 5: video aktarimi
		if tv.komut == "1":
			tv.sifir_noktasi = tv.basinc
			tv.paket_numarasi = 0
			tv.uydu_statusu = 1
		sleep(1)
