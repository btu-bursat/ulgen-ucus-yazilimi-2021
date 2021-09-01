#!/usr/bin/env python3
# Ulgen, 2021

import socket

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
	global motor_socket, motor_con

	try:
		f = open("/home/pi/ulgen/son_telemetri", "r")
		son_telemetri = f.read().split(",")
	except:
		son_telemetri = list()

	# Son telemetri verisi var ise oradan basla
	if len(son_telemetri) >= 18:
		takim_no = int(son_telemetri[0]) # 39374
		paket_numarasi = int(son_telemetri[1]) + 1
		gun, ay, yil = 0, 0, 0
		saat, dakika, saniye = 0, 0, 0
		basinc = float(son_telemetri[4])
		yukseklik = float(son_telemetri[5])
		inis_hizi = float(son_telemetri[6])
		sicaklik = float(son_telemetri[7])
		pil_gerilimi = float(son_telemetri[8])
		gps_latitude, gps_longitude, gps_altitude = float(son_telemetri[9]), float(son_telemetri[10]), float(son_telemetri[11])
		uydu_statusu = int(son_telemetri[12])
		pitch, roll, yaw = float(son_telemetri[13]), float(son_telemetri[14]), float(son_telemetri[15])
		donus_sayisi = int(son_telemetri[16])
		video_aktarim_bilgisi = str(son_telemetri[17])
	# Son telemetri verisi yok ise de her seyi sifirdan al
	else:
		takim_no = 39374
		paket_numarasi = 0
		gun, ay, yil = 0, 0, 0
		saat, dakika, saniye = 0, 0, 0
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

	# Yukseklik verisini hesaplamak icin sifir noktasini al
	sifir_noktasi = 1013.25
	try:
		f = open("/home/pi/ulgen/sifir_noktasi", "r")
		sifir_noktasi = f.read()
	except:
		sifir_noktasi = 1013.25

	ivme_x, ivme_y, ivme_z = 0, 0, 0
	komut = "0"
	telemetri_paketi = ""
	max_gerilim, min_gerilim = 4.2, 3.6
	gerilim_araligi = max_gerilim - min_gerilim
	pil_yuzde = 100

	# Motor kontrolu icin socket kutuphanesi kullanilarak haberlesilecek
	host = "0.0.0.0"
	port = 5000
	motor_socket = socket.socket()
	motor_socket.bind((host, port))
	motor_socket.listen(1)
	motor_con, addr = motor_socket.accept()
