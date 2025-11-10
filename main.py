from yardimci_modul import hosgeldin
class Kitap:
    def __init__(self,ad,yazar,mevcut=True):
        self.ad=ad
        self.yazar=yazar
        self.mevcut=mevcut
    def odunc_ver(self):
        self.mevcut=False
    def iade_al(self):
        self.mevcut=True
    def bilgi_yazdir(self):
        print(self.ad,self.yazar,self.mevcut)

class Kutuphane:
    def __init__(self):
        self.kitaplar=[]
        print("Kütüphane açıldı!")
        hosgeldin()
    def kitap_ekle(self,kitap):
        self.kitaplar.append(kitap)
    def kitap_sayisi(self):
        print(len(self.kitaplar))
    def kitaplari_sirala(self):
        sirali = sorted(self.kitaplar, key=lambda x: x.ad)
        print("Kitaplar (alfabetik sırayla):")
        for kitap in sirali:
            kitap.bilgi_yazdir()

    def __del__(self):
        print("Kütüphane kapandı!")
