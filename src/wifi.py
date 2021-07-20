import sensor_verileri as sv
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
		sv.komut = conn.recv(1024).decode()
		if not sv.komut:
			sv.komut = "0"
		# buraya video komutu oldugunu anlayacak ve videoyu alacak kod yazilacak
		# diger komutlari baska bir modul isleyecek
		conn.send(sv.telemetri_paketi.encode())
