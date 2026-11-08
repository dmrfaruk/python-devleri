from datetime import datetime

sinav = input("Sınav tarihini giriniz (GG/AA/YYYY SS:DD): ")
sinav_tarihi = datetime.strptime(sinav, "%d/%m/%Y %H:%M")

simdi = datetime.now()

fark = sinav_tarihi - simdi

gun = fark.days
saat = fark.seconds // 3600

print(f"Sınava {gun} gün {saat} saat kaldı.")