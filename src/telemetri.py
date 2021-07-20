#!/usr/bin/env python3

import telemetri_verileri as tv
import time
from datetime import datetime

def calistir():
	while True:
		baslangic = time.time()

		zaman = datetime.now()
		gun_ay_yil = str(zaman.day) + "/" + str(zaman.month) + "/" + str(zaman.year)
		saat_dakika_saniye = str(zaman.hour) + ":" + str(zaman.minute) + ":" + str(zaman.second)

		tv.telemetri_paketi  = ""
		tv.telemetri_paketi += tv.takim_no
		tv.telemetri_paketi += tv.paket_numarasi
		tv.telemetri_paketi += tv.gun_ay_yil
		tv.telemetri_paketi += tv.saat_dakika_saniye
		tv.telemetri_paketi += tv.basinc
		tv.telemetri_paketi += tv.yukseklik
		tv.telemetri_paketi += tv.inis_hizi
		tv.telemetri_paketi += tv.sicaklik
		tv.telemetri_paketi += tv.pil_gerilimi
		tv.telemetri_paketi += tv.gps_latitude
		tv.telemetri_paketi += tv.gps_longitude
		tv.telemetri_paketi += tv.gps_altitude
		tv.telemetri_paketi += tv.uydu_statusu
		tv.telemetri_paketi += tv.pitch
		tv.telemetri_paketi += tv.roll
		tv.telemetri_paketi += tv.yaw
		tv.telemetri_paketi += tv.donus_sayisi
		tv.telemetri_paketi += tv.video_aktarim_bilgisi

		with open("/home/pi/telemetri.txt", "a") as f:
			f.write(telemetri_paketi)
			break

		with open("/home/pi/son_telemetri", "a") as f:
			f.write(telemetri_paketi)
			break

		sure = time.time() - baslangic
		if sure < 1:
			time.sleep(1 - sure)
