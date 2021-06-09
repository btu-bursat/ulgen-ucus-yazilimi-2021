# BTÜ Bursat 1B Takımı 2021 Uçuş Yazılımı

BTÜ Bursat 1B takımının telemetri ve motor kontrolünü içeren uçuş yazılımı.

## Genel Bakış

Kart olarak `Raspberry Pi`, programlama dili olarak `Python 3` ve otonom olarak işlem yapması için de `Linux` tabanlı çözümler kullanıldı.

## Kurulum

İnternete bağlı `Raspberry Pi` üzerinde aşağıdaki komutları sırasıyla çalıştırın:

```bash
sudo apt install git
git clone https://github.com/Bursat/bursat-1b-ucus-yazilimi-2021.git
cd bursat-1b-ucus-yazilimi-2021
sudo ./kurulum.sh
```

## Telemetri Verileri

Telemetri verileri ayrı ayrı `/home/pi/telemetri_verileri` adlı dizinde toplanacaktır. Daha sonra bu veriler her saniye toplanıp, `telemetri.txt` adlı dosyada birleştirilecektir.
Telemetri verileri wi-fi ile aktarılacaktir.

### `telemetri_verileri` dizininin yapısı:

```
/home/pi/telemetri_verileri/
 |- takim_no
 |- paket_numarasi
 |- basinc
 |- yukseklik
 |- inis_hizi
 |- sicaklik
 |- pil_gerilimi
 |- gps_latitude
 |- gps_longitude
 |- gps_altitude
 |- uydu_statusu
 |- pitch
 |- roll
 |- yaw
 |- donus_sayisi
 |- video_aktarim_bilgisi
 |- telemetri.txt
```
