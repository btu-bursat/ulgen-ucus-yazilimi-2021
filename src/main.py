#!/usr/bin/env python3

from threading import Thread
import sensor_verileri as sv
import mpu9250
import bmp180

def main():
	sv.baslat()
	while True:
		pass
		#thr_wifi = Thread(target=)
		#thr_mpu9250 = Thread(target=mpu9250.calistir)
		#thr_bmp180 = Thread(target=bmp180.calistir)
		#thr_hiz = Thread(target=)

		#thr_wifi.start()
		#thr_mpu9250.start()
		#thr_bmp180.start()
		#thr_hiz.start()

		#thr_wifi.join()
		#thr_mpu9250.join()
		#thr_bmp180.join()
		#thr_hiz.join()

if __name__ == "__main__":
	main()
