#3. Hafta 2. Soru
#Sayı Tahmin Programı
sayi = 15
tahmin = 0
deneme_sayisi = 0
while sayi != tahmin:
    try:
        tahmin = int(input("Tahmininizi söyleyin(1-100 arası): "))
        deneme_sayisi += 1
        if tahmin > 100 or tahmin < 0:
            print("Lütfen doğru aralıkta tahmin giriniz.")
        elif tahmin > sayi:
            print("Fazla attın, azalt")
        elif tahmin < sayi:
            print("Artır, çok az geldi")
        else:
            print("Bildin.")
    except:
        print("Hata oluştu. Lütfen sayı giriniz")
print(deneme_sayisi, ". denemede bildiniz.", sep="")
