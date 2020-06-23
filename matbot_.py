import numpy as np

#ÖNEMLİ
#pip consol ile python paketlerini indirmeni sağlar
#Kodun çalışması için aramaya basıp cmd, yaz yönetici olarak çalıştır ve sonra "python -m pip install –upgrade pip && pip3 install numpy && echo BITTI" yaz, konsolda "BITTI" yazısını görünce kapat. Sonra kod düzgün çaışır
#Yoksa numpy'ı bulamaz
#Sonraki pip ile indirmelerede sadece "pip3 install paket adı" yazsan yeter (echo BITTI'nin sebebi eğer pip tam güncellemeden kapatırsan sadece silinik olarak kalır)

#Fikirler: 
# Farklı konular eklenebilir, 
# Farklı dersler eklenebilir,
# Wiki araması yaptrırlabilir,
# Denklem çözücü?,
# Arayüz
# /Aklına gelenleri buraya ekleyebilirsin/

#Şuanki özellikler: 
# Nerdeyse çoğu geometrik şeklin değerlerini bulabiliyoruz
# Konsol üzerinden fonksiyon çağırabiliyoruz
# Tamamiyle OOP(Object Oriented Programming)(Obje Tabanlı Programlama) ile yazıldı yani takibi ve yeni şeyler eklemesi kolay, hafifte olsa daha hızlı

from GeometrySolver import *

if(__name__ == "__main__"):

    YeniCozucu = GeometrySolver()
    fonksiyon = (str(input("Ne Cozmemi Istersiniz: ")).lower()).replace(" ", "").replace("_", "").replace("_", "")#Gereksiz karakterleri kaldırıyor

    #Verilen isim adında bir çözücü arayıyor ve bulursa çözüyor
    if(fonksiyon == "cember"):
        YeniCozucu.CemberCoz()
    elif(fonksiyon == "dortgen"):
        YeniCozucu.DortgenCoz()
    elif(fonksiyon == "ucgen"):
        YeniCozucu.UcgenCoz()
    elif(fonksiyon == "duzguncokgen"):
        YeniCozucu.DuzgunCokgenCoz()
    elif(fonksiyon == "yamuk"):
        YeniCozucu.YamukCoz()
    elif(fonksiyon == "eskenardortgen"):
        YeniCozucu.EskenarDortgenCoz()
    else:
        print("Bunun ne anlama geldiğini bilmiyorum")

# CLI'de yani command line interface(konsol arayüzü) çalışırken otomatik çıkmasını engeller
input("Cikmak icin herhangi bir tusa basın")
