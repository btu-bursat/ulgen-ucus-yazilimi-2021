# BTU Ulgen, 2021

from time import sleep

onceki_yukseklik = 0.0
olcekleme_zamani = 1
sifir_noktasi = 0

while True:
	with open("/home/pi/telemetri_verileri/yukseklik", "r") as f:
		onceki_yukseklik = f.read()
		break

# burasi duzenlenecek
while True:
	with open("/home/pi/telemetri_verileri/sifir_noktasi", "r") as f:
		sifir_noktasi = f.read()
		break
	try:
		sifir_noktasi = float(sifir_noktasi)
		break
	except:
		continue


while True:
	yukseklik = 0.0
	while True:
		with open("/home/pi/telemetri_verileri/yukseklik", "r") as f:
			yukseklik = f.read()
			break
	try:
		yukseklik = float(yukseklik)
	except:
		yukseklik = 0.0
	try:
		onceki_yukseklik = float(onceki_yukseklik)
	except:
		onceki_yukseklik = 0.0
	yukseklik_degisimi = yukseklik - onceki_yukseklik
	while True:
		with open("/home/pi/telemetri_verileri/inis_hizi", "w") as f:
			f.write(str(yukseklik_degisimi / olcekleme_zamani))
			break
	onceki_yukseklik = yukseklik
	sleep(olcekleme_zamani)
