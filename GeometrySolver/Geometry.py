import numpy as np

pi = 3.14 

#Çember
class Circle():
    def __init__(self, yari_cap, yay):  # Cember için gereken tüm parametreler
        __name__ = "__Cember__"
        self.r = yari_cap
        self.t = yay  # t, theta bilinmeyen açı yada parametre açı, sembolu 0 gibi bişey

    def YariCap(self):
        return self.r

    def Yay(self):
        return self.t/360

    def Cap(self):
        return self.YariCap() * 2

    def Cevre(self):
        return self.Yay() * (2 * pi * self.YariCap())

    def Alan(self):
        return self.Yay() * (np.power(self.YariCap() * pi, 2))  # np daha hızlı
#Dörtgen
class Quadrangle():
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
#Üçgen
class Triangle():
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
        return (self.Taban() * self.Yukseklik())/2
#Dörtgen
class Polygon():
    def __init__(self, kenar_sayisi, kenar_uzunlugu):
        __name__ = "__DuzgunCokgen__"
        self.ku = kenar_uzunlugu
        self.ks = kenar_sayisi

    def KenarUzunlugu(self):
        return self.ku

    def KenarSayisi(self):
        return self.ks

    def UcgenSayisi(self):
        return self.KenarSayisi() - 2

    def BirIcAci(self):
        return self.UcgenSayisi() * 180 / self.KenarSayisi()

    def BirDisAci(self):
        return 360 / self.KenarSayisi()

    def Cevre(self):
        return self.KenarSayisi() * self.KenarUzunlugu()

    def Alan(self):
        return self.KenarSayisi() * (np.power(self.KenarSayisi(), 2)) / (4 * np.tan(pi / self.KenarSayisi()))
#Yamuk
class Trapezoid():
    def __init__(self, a_uzunlugu, b_uzunlugu, c_uzunlugu, d_uzunlugu, yukseklik):
        __name__ = "__Yamuk__"
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
#Geometri Çözücü
class GeometrySolver():
    def __init__(self):
        __name__ = "__GeometrySolver__"

    def CemberCoz(self):
        yari_cap = float(input("Cemberin Yari Capi: "))
        yay = float(input("Cemberin Yay Acisi: "))

        NewCircle = Circle(yari_cap, yay)

        print("Cap: ", NewCircle.Cap())
        print("Cevre: ", NewCircle.Cevre())
        print("Alan: ", NewCircle.Alan())

    def DortgenCoz(self):
        kısa_kenar = float(input("Dortgenin Kisa Kenari: "))
        uzun_kenar = float(input("Dortgenin Uzun Kenari:"))

        NewQuadrangle = Quadrangle(kısa_kenar, uzun_kenar)

        print("Diagonal: ", NewQuadrangle.Diagonal())
        print("Cevre: ", NewQuadrangle.Cevre())
        print("Alan: ", NewQuadrangle.Alan())

    def UcgenCoz(self):
        a_kenarı = float(input("Ucgenin A Kenari Uzunlugu: "))
        b_kenarı = float(input("Ucgenin B Kenari(Tabanı) Uzunlugu: "))
        c_kenarı = float(input("Ucgenin C Kenari Uzunlugu: "))
        yuksekligi = float(input("Ucgenin Yuksekligi: "))

        NewTriangle = Triangle(a_kenarı, b_kenarı, c_kenarı, yuksekligi)

        print("Cevre: ", NewTriangle.Cevre())
        print("Alan: ", NewTriangle.Alan())

    def DuzgunCokgenCoz(self):
        kenar_sayisi = float(input("Cokgendeki Kenar Sayısı: "))
        kenar_uzunlugu = float(input("Cokgendeki Kenar Uzunlugu: "))

        NewPolygon = Polygon(kenar_sayisi, kenar_uzunlugu)

        print("Bir Ic Acisi: ", NewPolygon.BirIcAci())
        print("Bir Dis Acisi: ", NewPolygon.BirDisAci())
        print("Cevresi: ", NewPolygon.Cevre())
        print("Alani", NewPolygon.Alan())

    def YamukCoz(self):
        a_kenarı = float(input("Yamugun A Kenari Uzunlugu: "))
        b_kenarı = float(input("Yamugun B Kenari(Tabanı) Uzunlugu: "))
        c_kenarı = float(input("Yamugun C Kenari Uzunlugu: "))
        d_kenarı = float(input("Yamugun D Kenari Uzunlugu: "))
        yuksekligi = float(input("Yamugun Yuksekligi: "))

        NewTrapezoid = Trapezoid(a_kenarı, b_kenarı, c_kenarı, d_kenarı, yuksekligi)

        print("Cevre: ", NewTrapezoid.Cevre())
        print("Alan: ", NewTrapezoid.Alan())
