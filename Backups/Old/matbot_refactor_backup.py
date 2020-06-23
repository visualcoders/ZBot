import numpy as np

#ÖNEMLİ
#pip consol ile python paketlerini indirmeni sağlar
#Kodun çalışması için aramaya basıp cmd, yaz yönetici olarak çalıştır ve sonra "python -m pip install –upgrade pip && pip3 install numpy && echo BITTI" yaz, konsolda "BITTI" yazısını görünce kapat. Sonra kod düzgün çaışır
#Yoksa numpy'ı bulamaz
#Sonraki pip ile indirmelerede sadece "pip3 install paket adı" yazsan yeter (echo BITTI'nin sebebi eğer pip tam güncellemeden kapatırsan sadece silinik olarak kalır)

#Sabitler
pi = 3.14 

class Cember():
    def __init__(self, yari_cap, yay): #Cember için gereken tüm parametreler
        __name__ = "__Cember__"
        self.r = yari_cap 
        self.t = yay #t, theta bilinmeyen açı yada parametre açı, sembolu 0 gibi bişey
    
    def YariCap(self):
        return self.r
    def Yay(self):
        return self.t/360
    def Cap(self):
        return self.YariCap() * 2

    def Cevre(self):
        return self.Yay() * (2 * pi * self.YariCap())
    def Alan(self):
        return self.Yay() * (np.power(self.r * pi, 2))#np daha hızlı
class Dortgen():
    def __init__(self, uzunluk, yukseklik):
        __name__ = "__Dortgen__"
        self.u = uzunluk
        self.y = yukseklik

    def Uzunluk(self):
        return self.u
    def Yukseklik(self):
        return self.y
    
    def Diagonal(self):
        return np.sqrt(np.power(self.Uzunluk(), 2) + np.power(self.Yukseklik(), 2))
    def Cevre(self):
        return (self.Uzunluk() * 2) + (self.Yukseklik() * 2)
    def Alan(self):
        return self.Uzunluk() * self.Yukseklik()
class Ucgen():
    def __init__(self, a_uzunlugu, b_uzunlugu, c_uzunlugu, yukseklik):
        __name__ = "__Ucgen__"
        self.a = a_uzunlugu
        self.b = b_uzunlugu
        self.c = c_uzunlugu
        self.h = yukseklik

    def Yukseklik(self):
        return self.h
    def Taban(self):
        return self.b

    def Cevre(self):
        return self.a + self.b + self.c
    def Alan(self):
        return (self.Taban * self.Yukseklik)/2
class DuzgunCokgen():
    def __init__(self, kenar_sayisi, kenar_uzunlugu):
        __name__ = "__DuzgunCokgen__"
        self.ku = kenar_uzunlugu
        self.ks = kenar_sayisi

    def KenarUzunlugu(self):
        return self.ku
    def KenarSayisi(self):
        return self.ks

    def UcgenSayisi(self):
        return self.KenarSayisi - 2
    
    def BirIcAci(self):
        return self.UcgenSayisi * 180 / self.KenarSayisi
    def BirDisAci(self):
        return 360 / self.KenarSayisi

    def Cevre(self):
        return self.KenarSayisi * self.KenarUzunlugu
    def Alan(self):
        return self.KenarSayisi * (np.power(self.KenarSayisi, 2)) / (4 * np.tan(pi / self.KenarSayisi))
class Yamuk():
    def __init__(self, a_uzunlugu, b_uzunlugu, c_uzunlugu, d_uzunlugu, yukseklik):
        self.a = a_uzunlugu 
        self.b = b_uzunlugu
        self.c = c_uzunlugu
        self.d = d_uzunlugu
        self.h = yukseklik

        def Yukseklik(self):
            return self.h

        def Cevre(self):
            return self.a + self.b + self.c + self.d
        def Alan(self):
            return (self.a + self.b) / 2 * self.Yukseklik()
class Cozucu():
    def __init__(self):
        __name__ = "__Cozucu__"
        
    
    def CemberCoz(self):
        yari_cap = float(input("Cemberin Yari Capi: "))
        yay = float(input("Cemberin Yay Acisi: "))

        YeniCember = Cember(yari_cap, yay)

        print("Cap: ", YeniCember.Cap())
        print("Cevre: ", YeniCember.Cevre())
        print("Alan: ", YeniCember.Alan())

    def DortgenCoz(self):
        kısa_kenar = float(input("Dortgenin Kisa Kenari: "))
        uzun_kenar = float(input("Dortgenin Uzun Kenari:"))

        YeniDortgen = Dortgen(kısa_kenar, uzun_kenar)

        print("Diagonal: ", YeniDortgen.Diagonal())
        print("Cevre: ", YeniDortgen.Cevre())
        print("Alan: ", YeniDortgen.Alan())

    def UcgenCoz(self):
        a_kenarı = float(input("Ucgenin A Kenari Uzunlugu: "))
        b_kenarı = float(input("Ucgenin B Kenari(Tabanı) Uzunlugu: "))
        c_kenarı = float(input("Ucgenin C Kenari Uzunlugu: "))
        yuksekligi = float(input("Ucgenin Yuksekligi: "))

        YeniUcgen = Ucgen(a_kenarı, b_kenarı, c_kenarı, yuksekligi)

        print("Cevre: ", YeniUcgen.Cevre())
        print("Alan: ", YeniUcgen.Alan())

    def DuzgunCokgenCoz(self):
        kenar_sayisi = float(input("Cokgendeki Kenar Sayısı: "))
        kenar_uzunlugu = float(input("Cokgendeki Kenar Uzunlugu: "))

        YeniCokgen = DuzgunCokgen(kenar_sayisi, kenar_uzunlugu)

        print("Bir Ic Acisi: ", YeniCokgen.BirDisAci())
        print("Bir Dis Acisi: ", YeniCokgen.BirDisAci())
        print("Cevresi: ", YeniCokgen.Cevre())
        print("Alani", YeniCokgen.Alan())

    def YamukCoz(self):
        a_kenarı = float(input("Yamugun A Kenari Uzunlugu: "))
        b_kenarı = float(input("Yamugun B Kenari(Tabanı) Uzunlugu: "))
        c_kenarı = float(input("Yamugun C Kenari Uzunlugu: "))
        d_kenarı = float(input("Yamugun D Kenari Uzunlugu: "))
        yuksekligi = float(input("Yamugun Yuksekligi: "))

        YeniYamuk = Yamuk(a_kenarı, b_kenarı, c_kenarı, d_kenarı, yuksekligi)

        print("Cevre: ", YeniYamuk.Cevre())
        print("Alan: ", YeniYamuk.Alan())

if(__name__ == "__main__"):

    YeniCozucu = Cozucu()
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
    else:
        print("Bunun ne anlama geldiğini bilmiyorum")

# CLI'de yani command line interface(konsol arayüzü) çalışırken otomatik çıkmasını engeller
input("Cikmak icin herhangi bir tusa basın")
