# BTU Ulgen, 2021

from time import sleep

onceki_yukseklik = 0.0
zaman = 1

while True:
	with open("/home/pi/telemetri_verileri/yukseklik", "r") as f:
		onceki_yukseklik = f.read()

while True:
	yukseklik = 0.0
	while True:
		with open("/home/pi/telemetri_verileri/yukseklik", "r") as f:
			yukseklik = f.read()
			break
	yukseklik_degisimi = yukseklik - onceki_yukseklik
	while True:
		with open("/home/pi/telemetri_verileri/inis_hizi", "w") as f:
			f.write(yukseklik_degisimi / zaman)
			break
	onceki_yukseklik = yukseklik
	sleep(zaman)
