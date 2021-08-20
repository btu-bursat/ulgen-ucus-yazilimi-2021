#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import time

def calistir():
	while True:
		baslangic = time.time()

		tmp  = ""
		tmp += str(tv.takim_no) + ","
		tmp += str(tv.paket_numarasi) + ","
		tmp += str(zaman_damgasi()) + ","
		tmp += "%.2f" % tv.basinc + ","
		tmp += "%.2f" % tv.yukseklik + ","
		tmp += "%.2f" % tv.inis_hizi + ","
		tmp += "%.1f" % tv.sicaklik + ","
		tmp += "%.2f" % tv.pil_gerilimi + ","
		tmp += str(tv.gps_latitude) + ","
		tmp += str(tv.gps_longitude) + ","
		tmp += str(tv.gps_altitude) + ","
		tmp += str(tv.uydu_statusu) + ","
		tmp += "%.2f" % tv.pitch + ","
		tmp += "%.2f" % tv.roll + ","
		tmp += "%.2f" % tv.yaw + ","
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

def zaman_damgasi():
	return str(tv.gun) + "/" + str(tv.ay) + "/" + str(tv.yil) + "," + str(tv.saat) + ":" + str(tv.dakika) + ":" + str(tv.saniye)
