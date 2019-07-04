#3. Hafta 6. Soru
#Asal sayı kontrol programı
print("1 ve daha kucuk sayılar programdan çıkış yapar.")
while True:
    try:
        sayi = int(input("Bir sayı giriniz: "))
        asal_sayi_mi = True
        if sayi <= 1:
            print("Lütfen 1 den büyük bir sayı giriniz.")
            break
        for i in range(2, sayi):
            if sayi % i == 0:
                asal_sayi_mi = False
                break
        if asal_sayi_mi == True:
            print(sayi, "asal sayıdır.")
        else:
            print(sayi, "asal sayı değildir.")
    except:
        print("Lütfen sayısal girdi yapınız.")
