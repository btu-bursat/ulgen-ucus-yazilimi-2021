# BTÜ Ülgen Takımı 2021 Uçuş Yazılımı

2021 Teknofest Türksat Model Uydu Yarışması için, Bursa Teknik Üniversitesi Ülgen model uydu takımının yazmış olduğu uçuş yazılımıdır. Yazılım `Raspberry Pi Zero W` üzerinde çalışması için tasarlanmıştır. Yazılım takımın QR aşamasında elenmesi sebebi ile tamamlanmamıştır.

## UYARILAR

Bu kodun paylaşılma sebebi yarışmaya yeni girecek takımların düşük seviyede kodlama yapmadan da yarışma için kod yazabileceğini göstermektir. Ancak yarışma için `Raspberry Pi` üzerinde `Python` dilinin yavaş kalması, ileri seviye işlemler için yetersiz kalması ve `Raspberry Pi`'nin PWM sinyali gibi çıkışlarının verimli çalışmaması  sebebi ile **kullanılmamasını** şiddetle tavsiye ediyoruz. Her halükarda benzer bir yapı ile yarışmaya girmeye kararlı iseniz lütfen bu dizindeki kodları sadece ilham alma ve öğrenme amacı ile kullanın. Kodun birebir kopyalanması yarışmadan diskalifiye olmanıza sebep olabilir.

Yazılımın eksik kaldığı alanlar:

* Bu yazılım sadece kapalı alanda test edilmiştir.
* Otonom uçuş algoritması, pil gerilimi sensörü ve güç yönetimi algoritması implemente edilmemiştir.
* Thread'ler arası bilgi paylaşımı için kullandığımız yöntem tek çekirdekli işlemcide sorun çıkarmasa da çok çekirdekli işlemcilerde sorun çıkartabilir.
* Sensörlerden kalibre edilmemiş saf veri okunduğundan yer istasyonuna giden verilerde sapmalar oluyor.
* Yaw eksenindeki duruş açısı yerine anlık değişim ölçülüyor.

## Kurulum

```bash
sudo apt install git
git clone https://github.com/Bursat/ulgen-ucus-yazilimi-2021.git
cd ulgen-ucus-yazilimi-2021
sudo ./kurulum.sh
```

## Lisans

Lisans bilgisi için [tıklayın.](LICENSE)
