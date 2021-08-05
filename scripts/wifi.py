#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import socket
from time import sleep

def calistir():
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
		if tv.komut == "5":
			# video aktarimi burada olacak
			pass
		conn.send(tv.telemetri_paketi.encode())
