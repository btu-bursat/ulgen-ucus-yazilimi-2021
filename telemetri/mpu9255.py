# BTU Ulgen, 2021

from FaBo9Axis_MPU9250 import MPU9250
import time
import board
import adafruit_bmp280

mpu9250 = MPU9250()
i2c = board.I2C()
bmp180 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp180.sea_level_pressure = 1013.25

# dosyadan okuma basarili olana kadar okumaya calis
## !!! ancak burada buyuk bir sikinti var !!!
## eger bir sensor hata verirse diger calisan butun sensorlerden
## cevap alinamayacak 
## buna bi ara bakilmasi lazim
while True:
	while True:
		with open("/home/pi/telemetri_verileri/ivme_x", "w") as f:
			f.write("%f" % mpu9250.readAccel()['x'])
			break
	while True:
		with open("/home/pi/telemetri_verileri/ivme_y", "w") as f:
			f.write("%f" % mpu9250.readAccel()['y'])
			break
	while True:
		with open("/home/pi/telemetri_verileri/ivme_z", "w") as f:
			f.write("%f" % mpu9250.readAccel()['z'])
			break
	while True:
		with open("/home/pi/telemetri_verileri/pitch", "w") as f:
			f.write("%f" % mpu9250.readGyro()['x'])
			break
	while True:
		with open("/home/pi/telemetri_verileri/roll", "w") as f:
			f.write("%f" % mpu9250.readGyro()['y'])
			break
	while True:
		with open("/home/pi/telemetri_verileri/yaw", "w") as f:
			f.write("%f" % mpu9250.readGyro()['z'])
			break
	while True:
		with open("/home/pi/telemetri_verileri/sicaklik", "w") as f:
			f.write("%f" % bmp180.temperature)
			break
	while True:
		with open("/home/pi/telemetri_verileri/basinc", "w") as f:
			f.write("%f" % bmp180.pressure)
			break
	while True:
		with open("/home/pi/telemetri_verileri/yukseklik", "w") as f:
			f.write("%f" % bmp180.altitude)
			break
