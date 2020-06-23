from math import *

pi = 3.141592653589793

class Cember():
    __name__ = "__Cember__"

    def __init__(self, yari_cap, yay):
        self.r = yari_cap
        self.t = yay

    def YariCap(self):
        return r
    def Cap(self):
        return self.r * 2
    def Yay(self):
        return self.t/360
    def Alan(self): 
        return self.Yay() * (pi * self.r ** 2)
    def Cevre(self): 
        return self.Yay() * (2 * pi * self.r)

class Dortgen():
    __name__ = "__Dortgen__"

    def __init__(self, uzunluk, yukseklik):#k kısa u uzun kenar
        self.u = uzunluk
        self.y = yukseklik

    def Cevre(self):
        return (self.u * 2) + (self.y * 2)
    def Alan(self):
        return (self.u * self.y)
    def Diagonal(self):
        return sqrt(self.u * self.u + self.y * self.y)

class Ucgen():
    __name__ = "__Ucgen__"

    def __init__(self, a_kenar, b_kenar, c_kenar, yukseklik):
        self.a = a_kenar
        self.b = b_kenar
        self.c = c_kenar
        self.y = yukseklik
    def Cevre(self):
        return self.a + self.b + self.c
    def Alan(self):
        return (self.b * self.y)/2
        
class DuzgunCokgen():
    __name__ = "__DuzgunCokgen__"
    
    def __init__(self, gen_s, gen_u):
        self.ks = gen_s
        self.ku = gen_u

    def KenarUzunlugu(self):
        return self.ku
    def KenarSayısı(self):
        return self.ks
    def UcgenSayısı(self): 
        return self.ks - 2
    def BirIcAci(self):
        return self.UcgenSayısı * 180 / self.ks
    def BirDisAci(self):
        return 360 / self.ks
    def Alan(self):
        return self.ks * (self.ks * self.ks) / (4 * tan(pi / self.ks))
    def Cevre(self):
        return self.ks * self.ku

class Cozucu():
    def __init__(self):
        pass

    def CemberCozucu(self):
        yari_cap = float(input("Cemberinizin Yari Capi: "))
        yay = float(input("Cemberinizin Yayı (Eger istemiyorsanız 360 girin): "))

        YeniCember = Cember(yari_cap, yay)

        print("Cevre: ", YeniCember.Cevre())
        print("Alan: ", YeniCember.Alan())
    def DortgenCozucu(self):
        kısa_kenar = float(input("Dortgeninizin Kısa Kenarı: "))
        uzun_kenar = float(input("Dortgeninizin Uzun Kenarı: "))

        YeniDortgen = Dortgen(kısa_kenar, uzun_kenar)

        print("Cevre: ", YeniDortgen.Cevre())
        print("Diagonal: ", YeniDortgen.Diagonal())
        print("Alan: ", YeniDortgen.Alan())
    def UcgenCozucu(self):
        a_kenarı = float(input("Ucgeninizin A Kenarı: "))
        b_kenarı = float(input("Ucgeninizin B Kenarı(Tabanı): "))
        c_kenarı = float(input("Ucgeninizin C Kenarı: "))
        yuksekligi = float(input("Ucgeninizin Yuksekligi(Alan Icin): "))

        YeniUcgen = Ucgen(a_kenarı, b_kenarı, c_kenarı, yuksekligi)

        print("Cevre: ", YeniUcgen.Cevre())
        print("Alan: ", YeniUcgen.Alan())
    def DuzgunCokgenCozucu(self):
        gen_sayisi = float(input("Cokgendeki Gen Sayısı: "))
        gen_uzunlugu = float(input("Cokgendeki Gen Uzunlugu: "))

        YeniCokgen = DuzgunCokgen(gen_sayisi, gen_uzunlugu)

        print("Bir Ic Acisi: ", YeniCokgen.BirDisAci())
        print("Bir Dis Acisi: ", YeniCokgen.BirDisAci())
        print("Cevresi: ", YeniCokgen.Cevre())
        print("Alani", YeniCokgen.Alan())

if(__name__ == "__main__"):

    YeniCozucu = Cozucu()
    fonksiyon = str(input("Ne Cozmemi Istersiniz: ")).lower()

    if(fonksiyon == "cember"):
        YeniCozucu.CemberCozucu()
    elif(fonksiyon == "dortgen"):
        YeniCozucu.DortgenCozucu()
    elif(fonksiyon == "ucgen"):
        YeniCozucu.UcgenCozucu()
    elif(fonksiyon == "cokgen"):
        YeniCozucu.DuzgunCokgenCozucu()

input("Cikmak icin herhangi bir tusa basın")#CLI'de yani command line interface(konsol arayüzü) çalışırken otomatik çıkmasını engeller
exit()
