#!/usr/bin/env python3

import telemetri_verileri as tv
import motor
from time import sleep

def calistir():
	while True:
		if tv.uydu_statusu == "1":
			pass
		# devami da yazilacak
