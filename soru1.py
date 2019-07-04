#3. Hafta 1. Soru
#Kullanıcı Hesabı Oluşturma Programı
print("Hoşgeldiniz. Çıkmak için q ya basınız")
while True:
    kullanici_adi = input("Kullanıcı adı: ")
    parola  = input("Parola: ")
    if kullanici_adi == "q" or parola == "q":
        break
    try:
        dosya = open("hesaplar.txt", "a+")
        dosya.seek(0)
        eskiler = dosya.readlines()
        eskiden_alinmis_mi = False
        for kullanici in eskiler:
            if kullanici_adi in kullanici:
                print("Bu kullanici adi alınmıştır. Başka bir ad seçin.")
                eskiden_alinmis_mi = True
                break
        if eskiden_alinmis_mi == False:
            dosya.write(kullanici_adi + " : " + parola + "\n")
            print("Bilgileriniz başarılı olarak kaydedildi.")
            dosya.close()
    except:
        print("Bir hata oluştu.")
