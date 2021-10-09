#!/bin/bash
# Ulgen, 2021

# Eger script root izni ile calistirilmadi ise cikis yap
if [ "$EUID" -ne 0 ]
then
	echo "Kurulumun yapilabilmesi icin yonetici hakkina sahip olmaniz gerekmekte! Bunu deneyin: sudo $0"
	exit
fi

echo "Gerekli paketler yukleniyor..."
apt update
apt install -y python3-pip
pip3 install FaBo9Axis-MPU9250-python3
pip3 install adafruit-circuitpython-bmp280
pip3 install adafruit-circuitpython-pca9685
pip3 install adafruit-circuitpython-servokit

echo "Kodlar kopyalaniyor..."
mkdir -p /home/pi/ulgen/scripts/
cp scripts/* /home/pi/ulgen/scripts/

echo "Servis yukleniyor..."
cp ulgen.service /etc/systemd/system/ulgen.service

systemctl daemon-reload
systemctl enable ulgen
systemctl start ulgen

echo "Kurulum bitti"
