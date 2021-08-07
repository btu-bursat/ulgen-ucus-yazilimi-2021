#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import time
from datetime import datetime

def calistir():
	while True:
		baslangic = time.time()

		tmp  = ""
		tmp += str(tv.takim_no) + ","
		tmp += str(tv.paket_numarasi) + ","
		tmp += str(zaman_damgasi()) + ","
		tmp += str(tv.basinc) + ","
		tmp += str(tv.yukseklik) + ","
		tmp += str(tv.inis_hizi) + ","
		tmp += str(tv.sicaklik) + ","
		tmp += str(tv.pil_gerilimi) + ","
		tmp += str(tv.gps_latitude) + ","
		tmp += str(tv.gps_longitude) + ","
		tmp += str(tv.gps_altitude) + ","
		tmp += str(tv.uydu_statusu) + ","
		tmp += str(tv.pitch) + ","
		tmp += str(tv.roll) + ","
		tmp += str(tv.yaw) + ","
		tmp += str(tv.donus_sayisi) + ","
		tmp += str(tv.video_aktarim_bilgisi)

		tv.telemetri_paketi = tmp

		with open("/home/pi/telemetri.txt", "a") as f:
			f.write(tv.telemetri_paketi + "\n")

		with open("/home/pi/son_telemetri", "w") as f:
			f.write(tv.telemetri_paketi)

		tv.paket_numarasi = int(tv.paket_numarasi) + 1

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
