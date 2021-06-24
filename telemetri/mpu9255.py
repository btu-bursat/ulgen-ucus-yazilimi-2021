from FaBo9Axis_MPU9250 import MPU9250
import time
import board
import adafruit_bmp280

mpu9250 = MPU9250()
i2c = board.I2C()
bmp180 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp180.sea_level_pressure = 1013.25

while True:
    with open("/home/pi/telemetri_verileri/ivme_x", "w") as f:
        f.write("%f" % mpu9250.readAccel()['x'])
    with open("/home/pi/telemetri_verileri/ivme_y", "w") as f:
        f.write("%f" % mpu9250.readAccel()['y'])
    with open("/home/pi/telemetri_verileri/ivme_z", "w") as f:
        f.write("%f" % mpu9250.readAccel()['z'])
    with open("/home/pi/telemetri_verileri/pitch", "w") as f:
        f.write("%f" % mpu9250.readGyro()['x'])
    with open("/home/pi/telemetri_verileri/roll", "w") as f:
        f.write("%f" % mpu9250.readGyro()['y'])
    with open("/home/pi/telemetri_verileri/yaw", "w") as f:
        f.write("%f" % mpu9250.readGyro()['z'])
    with open("/home/pi/telemetri_verileri/sicaklik", "w") as f:
        f.write("%f" % bmp180.temperature)
    with open("/home/pi/telemetri_verileri/basinc", "w") as f:
        f.write("%f" % bmp180.pressure)
    with open("/home/pi/telemetri_verileri/yukseklik", "w") as f:
        f.write("%f" % bmp180.altitude)
