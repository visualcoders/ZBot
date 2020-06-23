

class Cokgen():
    __name__ = "Cokgen"

    def __init__(self, kenar_uzunlugu, kenar_sayısı):
                 self.ku = kenar_uzunlugu
                 self.ks = kenar_sayısı

    def KenarUzunlugu(self):
        return self.ku
    def KenarSayısı(self):
        return self.ks
    def Alan(self):
        return self.ku * self.ks

if(__name__ == "__main__"):
    kenar_uzunlugu =float(input("Cokgeninizin Kenar Uzunlugu: "))
    kenar_sayısı =float(input("Cokgeninizin Kenar Sayısı: "))

    YeniCokgen = Cokgen(kenar_uzunlugu, kenar_sayısı)

    print("Alan: ", YeniCokgen.Alan())
