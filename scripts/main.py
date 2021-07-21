#!/usr/bin/env python3

from threading import Thread
import telemetri_verileri as tv
import mpu9250
import bmp180
import gps
import pil_yuzde
import hiz
import telemetri
import wifi
import komut
import guc_yonetimi
import sis
import otonom_ucus
import motor

def thrd_fun(thread_fonksiyonu):
	def hata_denetleyici():
		while True:
			try:
				thread_fonksiyonu()
			except BaseException as e:
				with open("/home/pi/log.txt", "a") as f:
					f.write("{}: {} fonksiyonu '{}' hata mesaji ile coktu, yeniden baslatiliyor.\n".format(tv.zaman_damgasi(), thread_fonksiyonu.__name__, e))
			else:
				with open("/home/pi/log.txt", "a") as f:
					f.write("{}: {} fonksiyonu basari ile sonlandi.\n".format(tv.zaman_damgasi(), thread_fonksiyonu.__name__))
				break
	return hata_denetleyici

def main():
	tv.baslat()

	thrd_mpu9250 = Thread(target=thrd_fun(mpu9250.calistir))
	thrd_bmp180 = Thread(target=thrd_fun(bmp180.calistir))
	thrd_gps = Thread(target=thrd_fun(gps.calistir))
	thrd_pil_yuzde = Thread(target=thrd_fun(pil_yuzde.calistir))
	thrd_hiz = Thread(target=thrd_fun(hiz.calistir))
	thrd_telemetri = Thread(target=thrd_fun(hiz.calistir))
	thrd_wifi = Thread(target=thrd_fun(wifi.calistir))
	thrd_komut = Thread(target=thrd_fun(komut.calistir))
	thrd_guc_yonetimi = Thread(target=thrd_fun(guc_yonetimi.calistir))
	thrd_sis = Thread(target=thrd_fun(sis.calistir))
	thrd_otonom_ucus = Thread(target=thrd_fun(otonom_ucus.calistir))
	thrd_motor = Thread(target=thrd_fun(motor.calistir))

	thrd_mpu9250.start()
	thrd_bmp180.start()
	thrd_gps.start()
	thrd_pil_yuzde.start()
	thrd_hiz.start()
	thrd_telemetri.start()
	thrd_wifi.start()
	thrd_komut.start()
	thrd_guc_yonetimi.start()
	thrd_sis.start()
	thrd_otonom_ucus.start()
	thrd_motor.start()

if __name__ == "__main__":
	main()