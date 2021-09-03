#!/usr/bin/env python3
# Ulgen, 2021

from threading import Thread
from time import sleep
import telemetri_verileri as tv
import mpu9250
import bmp280
import gps
import pil_yuzde
import hiz
import telemetri
import wifi
import guc_yonetimi
import otonom_ucus
import yaw_donus
import log
import motor

# Bu fonksiyon thread fonksiyonlarinda yasanacak herhangi bir sikintida hatayi
# yakalayip SD karta hatayi yazar ve fonksiyonu bastan baslatir
def thrd_fun(sinif_ismi):
	def hata_denetleyici():
		bekleme_suresi = 0.5
		while True:
			try:
				sinif_ismi.calistir()
			except BaseException as e:
				log.logla("{} '{}' hata mesaji ile coktu, {} saniye icinde yeniden baslatiliyor.".format(sinif_ismi.__name__, e, bekleme_suresi))
				sleep(bekleme_suresi)
			else:
				log.logla("{} basari ile sonlandi.".format(sinif_ismi.__name__))
				break
	return hata_denetleyici

def main():
	# Telemetri verileri ayarlanir
	tv.baslat()

	# Thread'ler ayarlanir
	thrd_mpu9250 = Thread(target = thrd_fun(mpu9250))
	thrd_bmp280 = Thread(target = thrd_fun(bmp280))
	thrd_gps = Thread(target = thrd_fun(gps))
	thrd_pil_yuzde = Thread(target = thrd_fun(pil_yuzde))
	thrd_hiz = Thread(target = thrd_fun(hiz))
	thrd_telemetri = Thread(target = thrd_fun(telemetri))
	thrd_wifi = Thread(target = thrd_fun(wifi))
	thrd_guc_yonetimi = Thread(target = thrd_fun(guc_yonetimi))
	thrd_otonom_ucus = Thread(target = thrd_fun(otonom_ucus))
	thrd_yaw_donus = Thread(target = thrd_fun(yaw_donus))
	thrd_motor = Thread(target = thrd_fun(motor))

	# Thread'ler baslatilir
	thrd_mpu9250.start()
	thrd_bmp280.start()
	thrd_gps.start()
	thrd_pil_yuzde.start()
	thrd_hiz.start()
	thrd_telemetri.start()
	thrd_wifi.start()
	thrd_guc_yonetimi.start()
	thrd_otonom_ucus.start()
	thrd_yaw_donus.start()
	thrd_motor.start()

	log.logla("Butun thread'lere baslangic verildi.")

if __name__ == "__main__":
	main()
