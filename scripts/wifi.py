#!/usr/bin/env python3 Ulgen, 2021

import telemetri_verileri as tv
import socket
from time import sleep
import log

def calistir():
	# Yer istasyonu ile baglanti kurmak icin socket kutuphanesi kullanilir
	host = "0.0.0.0"
	port = 5003
	uydu_socket = socket.socket()
	uydu_socket.bind((host, port))
	uydu_socket.listen(1)
	conn, addr = uydu_socket.accept()

	while True:
		tv.komut = conn.recv(1024).decode()
		if not tv.komut:
			tv.komut = "0"

		# Kalibre et komutu
		if tv.komut == "1":
			tv.sifir_noktasi = tv.basinc
			try:
				f = open("/home/pi/ulgen/sifir_noktasi", "w")
				f.write(str(tv.sifir_noktasi))
			except:
				log.logla("Sifir noktasi SD karta yazilamadi.")
			tv.paket_numarasi = 1
			tv.uydu_statusu = 1

		# Yer istasyonundan uyduya video aktarimi komutu
		elif tv.komut[0] == "5":
			boyut = int(tv.komut.split(" ")[1])
			parca = boyut // 1024
			if boyut % 1024 != 0:
				parca += 1
			video = bytes()
			for i in range(parca + 1):
				video += conn.recv(1024)
			with open("/home/pi/ulgen/video.mp4", "wb") as f:
				f.write(video)

		# Telemetri paketini yer istasyonuna gonder
		conn.send(tv.telemetri_paketi.encode())
