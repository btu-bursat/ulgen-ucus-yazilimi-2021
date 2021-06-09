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

	with open("/home/pi/telemetri_verileri/uydu_statusu", "r") as f:
		uydu_statusu = f.read()

	zaman = datetime.datetime.now()
	gun_ay_yil = str(zaman.day) + "/" + str(zaman.month) + "/" + str(zaman.year)
	saat_dakika_saniye = str(zaman.hour) + "/" + str(zaman.minute) + "/" + str(zaman.second)

	telemetri  = takim_no + "," + paket_numarasi + "," + uydu_statusu + ","
	telemetri += gun_ay_yil + "," + saat_dakika_saniye
	telemetri += "\n"

	with open("/home/pi/telemetri_verileri/telemetri.txt", "at") as tf:
		tf.write(telemetri)

	# 1 Hz de calismak icin dandik bir deneme; daha iyisini bulduysaniz bana bi
	# selam cakin
	exec_time = time.time() - start_time
	if exec_time < 1:
		time.sleep(1 - exec_time)
