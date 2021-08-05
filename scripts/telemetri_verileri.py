#!/usr/bin/env python3

def baslat():
	global takim_no
	global paket_numarasi
	global basinc
	global yukseklik
	global inis_hizi
	global sicaklik
	global pil_gerilimi
	global gps_latitude, gps_longitude, gps_altitude
	global uydu_statusu
	global pitch, roll, yaw
	global donus_sayisi
	global video_aktarim_bilgisi
	global ivme_x, ivme_y, ivme_z
	global sifir_noktasi
	global komut
	global telemetri_paketi
	global max_gerilim, min_gerilim
	global gerilim_araligi
	global pil_yuzde
	global saat, dakika, saniye
	global gun, ay, yil

	with open("/home/pi/son_telemetri", "r") as f:
		son_telemetri = f.read().split(",")

	if len(son_telemetri) <= 1:
		return

	takim_no = 39374
	paket_numarasi = son_telemetri[1]
	gun, ay, yil = 0, 0, 0
	saat, dakika, saniye = 0, 0, 0
	basinc = son_telemetri[4]
	yukseklik = son_telemetri[5]
	inis_hizi = son_telemetri[6]
	sicaklik = son_telemetri[7]
	pil_gerilimi = son_telemetri[8]
	gps_latitude, gps_longitude, gps_altitude = son_telemetri[9], son_telemetri[10], son_telemetri[11]
	uydu_statusu = son_telemetri[12]
	pitch, roll, yaw = son_telemetri[13], son_telemetri[14], son_telemetri[15]
	donus_sayisi = son_telemetri[16]
	video_aktarim_bilgisi = son_telemetri[17]
	ivme_x, ivme_y, ivme_z = 0, 0, 0
	# !!!!!!
	# sifir noktasindaki basınç sd karta da yazılıp oradan okunmalı
	sifir_noktasi = 1013.25
	komut = "0"
	telemetri_paketi = ""
	max_gerilim, min_gerilim = 4.2, 3.6
	gerilim_araligi = max_gerilim - min_gerilim
	pil_yuzde = 100
