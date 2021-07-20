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

	with open("/home/pi/son_telemetri", "r") as f:
			son_telemetri = f.write()
	# son telemetri verisi parcalara ayrilip asagidaki degiskenlere atanacak
	
	takim_no = 12345
	paket_numarasi = 0
	basinc = 0
	yukseklik = 0
	inis_hizi = 0
	sicaklik = 0
	pil_gerilimi = 0
	gps_latitude, gps_longitude, gps_altitude = 0, 0, 0
	uydu_statusu = 1
	pitch, roll, yaw = 0, 0, 0
	donus_sayisi = 0
	video_aktarim_bilgisi = "Hayir"
	ivme_x, ivme_y, ivme_z = 0, 0, 0
	sifir_noktasi = 0
	komut = 0
	telemetri_paketi = ""
	max_gerilim, min_gerilim = 4.2, 3.6
	gerilim_araligi = max_gerilim - min_gerilim
	pil_gerilim = max_gerilim
	pil_yuzde = 100
