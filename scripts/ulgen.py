#!/usr/bin/env python3
# Ulgen, 2021

from threading import Thread
from time import sleep
import telemetri_verileri as tv
import mpu9250
import bmp180
import gps
import pil_yuzde
import hiz
import telemetri
import wifi
import guc_yonetimi
import otonom_ucus
import yaw_donus
import log

def thrd_fun(sinif_ismi, thread_fonksiyonu):
	def hata_denetleyici():
		while True:
			try:
				thread_fonksiyonu()
			except BaseException as e:
				log.logla("{} sinifindan {} fonksiyonu '{}' hata mesaji ile coktu, yeniden baslatiliyor.".format(sinif_ismi.__name__, thread_fonksiyonu.__name__, e))
				sleep(0.5)
			else:
				log.logla("{} sinifindan {} fonksiyonu basari ile sonlandi.".format(sinif_ismi.__name__, thread_fonksiyonu.__name__))
				break
	return hata_denetleyici

def main():
	tv.baslat()

	thrd_mpu9250 = Thread(target=thrd_fun(mpu9250, mpu9250.calistir))
	thrd_bmp180 = Thread(target=thrd_fun(bmp180, bmp180.calistir))
	thrd_gps = Thread(target=thrd_fun(gps, gps.calistir))
	thrd_pil_yuzde = Thread(target=thrd_fun(pil_yuzde, pil_yuzde.calistir))
	thrd_hiz = Thread(target=thrd_fun(hiz, hiz.calistir))
	thrd_telemetri = Thread(target=thrd_fun(telemetri, telemetri.calistir))
	thrd_wifi = Thread(target=thrd_fun(wifi, wifi.calistir))
	thrd_guc_yonetimi = Thread(target=thrd_fun(guc_yonetimi, guc_yonetimi.calistir))
	thrd_otonom_ucus = Thread(target=thrd_fun(otonom_ucus, otonom_ucus.calistir))
	thrd_yaw_donus = Thread(target=thrd_fun(yaw_donus, yaw_donus.calistir))

	thrd_mpu9250.start()
	thrd_bmp180.start()
	thrd_gps.start()
	thrd_pil_yuzde.start()
	thrd_hiz.start()
	thrd_telemetri.start()
	thrd_wifi.start()
	thrd_guc_yonetimi.start()
	thrd_otonom_ucus.start()
	thrd_yaw_donus.start()

	log.logla("Ana yazilim calismaya basladi.")
	print("hazir")

if __name__ == "__main__":
	main()
