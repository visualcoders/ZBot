
class Ucgen():
    __name__= "Ucgen"

    def __init__(self, yukseklik, taban):
        self.h = yukseklik
        self.b =taban


    def Yukseklik(self):
        return self.h
    def Taban(self):
        return self.b
    def Alan(self):
        return self.h * self.b

if(__name__=="__main__"):
    yukseklik = float(input("Ucgeninizin Yuksekligi: "))
    taban = float(input("Ucgeninizin Taban Uzunlugu: "))


    YeniUcgen = Ucgen(yukseklik, taban)

    print("Alan: ", YeniUcgen.Alan())
