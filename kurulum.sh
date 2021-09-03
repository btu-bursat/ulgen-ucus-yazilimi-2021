#!/bin/bash
# Ulgen, 2021

# Servislerin kurulabilmesi icin root haklarina sahip olmak gerekiyor
if [ "$EUID" -ne 0 ]
then
	echo "Kurulumun yapilabilmesi icin yonetici hakkina sahip olmaniz gerekmekte! Bunu deneyin: sudo $0"
	exit
fi

# Sistemin guncellenmesi ve gerekli yazilimlarin kurulmasi
echo "Gerekli paketler yukleniyor..."
#apt update
#apt install -y python3-pip
#pip3 install FaBo9Axis-MPU9250-python3
#pip3 install adafruit-circuitpython-bmp280
#pip3 install adafruit-circuitpython-pca9685
#pip3 install adafruit-circuitpython-servokit

# Butun kodlar /home/pi/ dizine tasinir
echo "Kodlar kopyalaniyor..."
mkdir -p /home/pi/ulgen/scripts/
cp scripts/* /home/pi/ulgen/scripts/

# Servislerin yuklenmesi
echo "Servisler yukleniyor..."
cp servisler/* /etc/systemd/system/

# Servislerin etkinlestirilmesi
systemctl daemon-reload

systemctl enable ulgen
systemctl enable motor

systemctl start ulgen
systemctl start motor

echo "Kurulum bitti"
