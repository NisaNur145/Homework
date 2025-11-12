import random
#Fibonacci Dizisi
liste=[0,1]
sayi=int(input("Sayi Giriniz"))
print(0)
print(1)
for i in range(0,sayi-2):
   c=liste[-1]+liste[-2]
   liste.append(c)
   print(c)

#Sayi Tahmin Oyunu
rastgele=random.randint(1,100)
tahmin=int(input("1-100 arasında tuttuğum sayiyi tahmin et:)"))
while rastgele!=tahmin:
    if tahmin>rastgele:
        print("Tuttuğum sayı daha küçük")
    if tahmin<rastgele:
        print("Tuttuğum sayı daha büyük")
    tahmin = int(input("Tekrar dene"))
if tahmin==rastgele:
    print(f"Bildin! Tuttuğum sayi {rastgele} idi!")

#Kelime Değiştirme
metin=input("Bir kelime girin!")
yeni_metin=""
for harf in metin:
    if harf in ["a","e","ı","i","o","ö","u","ü"]:
        yeni_metin+="*"
    else:
        yeni_metin+="#"
print(yeni_metin)

#Taş Kağıt Makas Oyunu
round_sayisi=int(input("Taş Kağıt Makasa Hoşgeldin! Kaç round oynamak istiyorsun?"))
kullanici_secimleri=[]
bilgisayar_secimleri=[]
sonuc=[]
skor={"kullanıcı":0,"bilgisayar":0}
ifadeler=["taş","kağıt","makas"]
for i in range(0,round_sayisi):
    kullanici_secimi=input("Birini seç: 'taş, kağıt, makas' ")
    bilgisayar_secimi=random.choice(ifadeler)
    if kullanici_secimi not in ifadeler:
        kullanici_secimi = input("Yanlış ifade girdiniz! Tekrar deneyin: ('taş', 'kağıt', 'makas')")
    else:
        if kullanici_secimi=="taş" and bilgisayar_secimi=="makas":
            sonuc.append("Kazandın!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            skor["kullanıcı"]+=1
            print("Kazandın!")
        elif kullanici_secimi=="makas" and bilgisayar_secimi=="kağıt":
            sonuc.append("Kazandın!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            skor["kullanıcı"]+=1
            print("Kazandın!")
        elif kullanici_secimi=="kağıt" and bilgisayar_secimi=="taş":
            sonuc.append("Kazandın!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            skor["kullanıcı"]+=1
            print("Kazandın!")
        elif kullanici_secimi=="kağıt" and bilgisayar_secimi=="makas":
            sonuc.append("Kaybettin!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            skor["bilgisayar"]+=1
            print("Kaybettin!")
        elif kullanici_secimi=="makas" and bilgisayar_secimi=="taş":
            sonuc.append("Kaybettin!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            skor["bilgisayar"]+=1
            print("Kaybettin!")
        elif kullanici_secimi=="taş" and bilgisayar_secimi=="kağıt":
            sonuc.append("Kaybettin!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            skor["bilgisayar"]+=1
            print("Kaybettin!")
        elif kullanici_secimi=="kağıt" and bilgisayar_secimi=="kağıt":
            sonuc.append("Berabere!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            print("Berabere!")
        elif kullanici_secimi=="makas" and bilgisayar_secimi=="makas":
            sonuc.append("Berabere!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            print("Berabere!")
        elif kullanici_secimi=="taş" and bilgisayar_secimi=="taş":
            sonuc.append("Berabere!")
            kullanici_secimleri.append(kullanici_secimi)
            bilgisayar_secimleri.append(bilgisayar_secimi)
            print("Berabere!")
if skor["kullanıcı"]>skor["bilgisayar"]:
    kazanan="Kazandın!"
elif skor["kullanıcı"]<skor["bilgisayar"]:
    kazanan="Kaybettin!"
else:
    kazanan="Beraberlik!"
print("Oyun Bitti")
print(f"Oyun Skoru: {skor}")
print(f"Kazanan: {kazanan}")
print(f"kullanıcı seçimleri: {kullanici_secimleri}")
print(f"bilgisayar seçimleri: {bilgisayar_secimleri}")
