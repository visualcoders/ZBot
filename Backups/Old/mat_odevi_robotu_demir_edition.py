


class Dortgen():
    __name__="Dortgen"

    def __init__(self, kısa_kenar, uzun_kenar):
        self.kk = kısa_kenar
        self.uk = uzun_kenar

    def UzunKenar(self):
        return self.uk
    def Kısakenar(self):
        return self.kk
    def Alan(self):
        return self.uk * self.kk
    def Cevre(self):
        return (self.uk * 2) + (self.kk * 2)
if(__name__=="__main__"):
    kısa_kenar = float(input("Dörtgeninizin Kısa Kenarı: "))
    uzun_kenar = float(input("Dörtgeninizin Uzun Kenarı: "))

    YeniDortgen = Dortgen(kısa_kenar, uzun_kenar)

    print("Alan: ", YeniDortgen.Alan())
    print("Cevre: ", YeniDortgen.Cevre())
