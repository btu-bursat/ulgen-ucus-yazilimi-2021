#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
from time import sleep

def calistir():
	return
	while True:
		if tv.uydu_statusu == "1":
			if tv.ivme_y < 0 and tv.yukseklik >= 400:
				tv.uydu_statusu = "2"
		elif tv.uydu_statusu == "2":
			if tv.ivme_y < 0 and tv.yukseklik <= 400:
				tv.uydu_statusu = "3"
		elif tv.uydu_statusu == "3":
			pass
		# devami da yazilacak
