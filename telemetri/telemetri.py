import datetime
import time

while True:
	start_time = time.time()

	with open("/home/pi/telemetri_verileri/takim_no", "r") as f:
		takim_no = f.read()

	with open("/home/pi/telemetri_verileri/paket_numarasi", "r") as f:
		paket_numarasi = f.read()

	with open("/home/pi/telemetri_verileri/paket_numarasi", "w") as f:
		f.write(str(int(paket_numarasi) + 1))

	with open("/home/pi/telemetri_verileri/basinc", "r") as f:
		basinc = f.read()

	with open("/home/pi/telemetri_verileri/yukseklik", "r") as f:
		yukseklik = f.read()

	with open("/home/pi/telemetri_verileri/inis_hizi", "r") as f:
		inis_hizi = f.read()

	with open("/home/pi/telemetri_verileri/sicaklik", "r") as f:
		sicaklik = f.read()

	with open("/home/pi/telemetri_verileri/pil_gerilimi", "r") as f:
		pil_gerilimi = f.read()

	with open("/home/pi/telemetri_verileri/gps_latitude", "r") as f:
		gps_latitude = f.read()

	with open("/home/pi/telemetri_verileri/gps_longitude", "r") as f:
		gps_longitude = f.read()

	with open("/home/pi/telemetri_verileri/gps_altitude", "r") as f:
		gps_altitude = f.read()

	with open("/home/pi/telemetri_verileri/uydu_statusu", "r") as f:
		uydu_statusu = f.read()

	with open("/home/pi/telemetri_verileri/pitch", "r") as f:
		pitch = f.read()

	with open("/home/pi/telemetri_verileri/roll", "r") as f:
		roll = f.read()

	with open("/home/pi/telemetri_verileri/yaw", "r") as f:
		yaw = f.read()

	with open("/home/pi/telemetri_verileri/donus_sayisi", "r") as f:
		donus_sayisi = f.read()

	with open("/home/pi/telemetri_verileri/video_aktarim_bilgisi", "r") as f:
		video_aktarim_bilgisi = f.read()

	zaman = datetime.datetime.now()
	gun_ay_yil = str(zaman.day) + "/" + str(zaman.month) + "/" + str(zaman.year)
	saat_dakika_saniye = str(zaman.hour) + "/" + str(zaman.minute) + "/" + str(zaman.second)

	telemetri  = takim_no + "," + paket_numarasi + ","
	telemetri += gun_ay_yil + "," + saat_dakika_saniye + "," + basinc + ","
	telemetri += yukseklik + "," + inis_hizi + "," + sicaklik + ","
	telemetri += pil_gerilimi + "," + gps_latitude + ","
	telemetri += gps_longitude + "," + gps_altitude + ","
	telemetri += uydu_statusu + "," + pitch + "," + roll + "," + yaw + ","
	telemetri += donus_sayisi + "," + video_aktarim_bilgisi
	telemetri += "\n"

	with open("/home/pi/telemetri_verileri/telemetri.txt", "at") as tf:
		tf.write(telemetri)

	# 1 Hz de calismak icin dandik bir deneme; daha iyisini bulduysaniz bana bi
	# selam cakin
	# Eger calismasi 1 saniyeden uzun surerse bekleme yok
	exec_time = time.time() - start_time
	if exec_time < 1:
		time.sleep(1 - exec_time)
