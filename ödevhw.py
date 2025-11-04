#soru 1
a=int(input("Bir a sayisi giriniz: "))
b=int(input("Bir b sayisi giriniz: "))
c=a #a'nın değerini c de sakladım
a=b #b'nın değerini a ya atadım
b=c #a'nın değerini b ye atadım
print(f"a = {a}, b = {b}")

#soru 2
cumle=input("Cumle giriniz: ")
ilk_harf=cumle[0]
son_harf=cumle[len(cumle)-1]
length=len(cumle)
ters=cumle[::-1]
print("cümlenin ilk harfi:", ilk_harf)
print("son harfi:", son_harf)
print("cümlenin uzunluğu:", length)
print("Cümlenin tersi:" , ters )

#soru 3
islem=input("işlem giriniz: ")
if islem=="toplama" or islem=="çıkarma" or islem=="çarpma" or islem=="bölme":
    sayi1=int(input("Birinci sayiyi giriniz: "))
    sayi2=int(input("İkinci sayiyi giriniz: "))
    if islem=="toplama":
        print("Toplama sonucu: ",sayi1+sayi2)
    elif islem=="çıkarma":
        print("Çıkarma sonucu: ",sayi1-sayi2)
    elif islem=="çarpma":
        print("Çarpma sonucu: ",sayi1*sayi2)
    elif islem=="bölme" and sayi2==0:
        print("O ile bölme yapılamaz!")
    else:
        print("Bölme sonucu:", sayi1/sayi2)
else:
    print("Hatalı İşlem girdiniz!")

#soru 4
kenar1=int(input("1. kenarı giriniz: "))
kenar2=int(input("2. kenarı giriniz: "))
kenar3=int(input("3. kenarı giriniz: "))
toplam12=kenar1+kenar2
toplam13=kenar1+kenar3
toplam23=kenar3+kenar2
fark12=abs(kenar1-kenar2)
fark13=abs(kenar1-kenar3)
fark23=abs(kenar3-kenar2)
if kenar1>fark23 and kenar1<toplam23 and kenar2>fark13 and kenar3>fark12 and kenar2<toplam13 and kenar3<toplam12:
    if kenar1==kenar2 and kenar3==kenar2:
        print("Girdiğiniz üçgen eşkenardır ")
    elif kenar1==kenar2 or kenar3==kenar2 or kenar3==kenar1:
        print("Girdiğiniz üçgen ikizkenardır ")
    else:
        print("Girdiğiniz üçgen çeşitkenardır ")
else:
    print("Girdiğiniz değerler üçgen oluşturmaz!")

#soru 5
yeni_sayi=int(input("Bir sayi giriniz: "))
if (yeni_sayi**0.5)%1==0:
    print("Sayiniz tam kare sayıdır")
else:
    print("Sayiniz tam kare değildir!")
