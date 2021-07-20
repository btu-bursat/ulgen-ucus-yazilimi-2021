#!/usr/bin/env python3

from threading import Thread
from datetime import datetime
import telemetri_verileri as tv
import mpu9250
import bmp180
import pil_yuzde
import hiz
import telemetri
import wifi
import kalibre
import guc_yonetimi
import otonom_ucus

def thrd_fun(thread_fonksiyonu):
	def hata_denetleyici():
		while True:
			try:
				thread_fonksiyonu()
			except BaseException as e:
				zaman = datetime.now()
				zaman_damgasi  = str(zaman.day) + "/" + str(zaman.month) + "/" + str(zaman.year)
				zaman_damgasi += ", "
				zaman_damgasi += str(zaman.hour) + ":" + str(zaman.minute) + ":" + str(zaman.second)
				with open("/home/pi/log.txt", "a") as f:
					f.write("{}: {} fonksiyonu '{}' hata mesaji ile coktu, yeniden baslatiliyor.\n".format(zaman_damgasi, thread_fonksiyonu.__name__, e))
			else:
				zaman = datetime.now()
				zaman_damgasi  = str(zaman.day) + "/" + str(zaman.month) + "/" + str(zaman.year)
				zaman_damgasi += ", "
				zaman_damgasi += str(zaman.hour) + ":" + str(zaman.minute) + ":" + str(zaman.second)
				with open("/home/pi/log.txt", "a") as f:
					f.write("{}: {} fonksiyonu basari ile sonlandi.\n".format(zaman_damgasi, thread_fonksiyonu.__name__))
				break
	return hata_denetleyici

def main():
	tv.baslat()

	thrd_mpu9250 = Thread(target=thrd_fun(mpu9250.calistir))
	thrd_bmp180 = Thread(target=thrd_fun(bmp180.calistir))
	thrd_pil_yuzde = Thread(target=thrd_fun(pil_yuzde.calistir))
	thrd_hiz = Thread(target=thrd_fun(hiz.calistir))
	thrd_telemetri = Thread(target=thrd_fun(hiz.calistir))
	thrd_wifi = Thread(target=thrd_fun(wifi.calistir))
	thrd_kalibre = Thread(target=thrd_fun(komutlar.calistir))
	thrd_guc_yonetimi = Thread(target=thrd_fun(guc_yonetimi.calistir))
	thrd_otonom_ucus = Thread(target=thrd_fun(otonom_ucus.calistir))

	thrd_mpu9250.start()
	thrd_bmp180.start()
	thrd_pil_yuzde.start()
	thrd_hiz.start()
	thrd_telemetri.start()
	thrd_wifi.start()
	thrd_kalibre.start()
	thrd_guc_yonetimi.start()
	thrd_otonom_ucus.start()

	while True:
		if not thrd_mpu9250.is_alive():
			thrd_mpu9250.start()

if __name__ == "__main__":
	main()
