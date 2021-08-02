#!/usr/bin/env python3

import telemetri_verileri as tv
import time
from datetime import datetime

def calistir():
	while True:
		baslangic = time.time()

		tv.telemetri_paketi  = ""
		tv.telemetri_paketi += tv.takim_no
		tv.telemetri_paketi += tv.paket_numarasi
		tv.telemetri_paketi += zaman_damgasi()
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

		with open("/home/pi/son_telemetri", "w") as f:
			f.write(telemetri_paketi)

		sure = time.time() - baslangic
		if sure < 1:
			time.sleep(1 - sure)

# burasi gps sensorundeki saat verisi ile degisebilir
def zaman_damgasi():
	return str(tv.gun) + "/" + str(tv.ay) + "/" + str(tv.yil) + "," + str(tv.saat) + ":" + str(tv.dakika) + ":" + str(tv.saniye)
	"""zaman = datetime.now()
	gun_ay_yil = str(zaman.day) + "/" + str(zaman.month) + "/" + str(zaman.year)
	saat_dakika_saniye = str(zaman.hour) + ":" + str(zaman.minute) + ":" + str(zaman.second)
	return gun_ay_yil + "," + saat_dakika_saniye
	"""
