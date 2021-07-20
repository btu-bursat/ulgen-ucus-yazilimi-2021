#!/usr/bin/env python3

from threading import Thread
import sensor_verileri
import mpu9250
import bmp180

def main():
	sensor_verileri.baslat()
	while True:
		#thr_wifi = Thread(target=)
		#thr_mpu9250 = Thread(target=calistir)
		#thr_bmp180 = Thread(target=calistir)
		#thr_hiz = Thread(target=)
		#thr_wifi.start()
		#thr_mpu9250.start()
		#thr_bmp180.start()
		#thr_hiz.start()

if __name__ == "__main__":
	main()
