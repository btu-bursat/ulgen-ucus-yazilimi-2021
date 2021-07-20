#!/usr/bin/env python3

from threading import Thread
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

def main():
	tv.baslat()

	thrd_mpu9250 = Thread(target=mpu9250.calistir)
	thrd_bmp180 = Thread(target=bmp180.calistir)
	thrd_pil_yuzde = Thread(target=pil_yuzde.calistir)
	thrd_hiz = Thread(target=hiz.calistir)
	thrd_telemetri = Thread(target=hiz.calistir)
	thrd_wifi = Thread(target=wifi.calistir)
	thrd_kalibre = Thread(target=komutlar.calistir)
	thrd_guc_yonetimi = Thread(target=guc_yonetimi.calistir)
	thrd_otonom_ucus = Thread(target=otonom_ucus.calistir)

	thrd_mpu9250.start()
	thrd_bmp180.start()
	thrd_pil_yuzde.start()
	thrd_hiz.start()
	thrd_telemetri.start()
	thrd_wifi.start()
	thrd_kalibre.start()
	thrd_guc_yonetimi.start()
	thrd_otonom_ucus.start()

	#thrd_mpu9250.join()

if __name__ == "__main__":
	main()
