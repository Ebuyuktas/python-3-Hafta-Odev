#3. Hafta 4. Soru
#Alan-Hacim Hesaplama Programı
while True:
    print("""
Alan-Hacim Hesaplama:
    Alanlar:
    Karenin Alanı için      1
    Üçgenin Alanı için      2
    Dikdörtgenin Alanı için 3

    Hacimler:
    Küp Hacmi için          4
    Küre Hacmi için         5
    Koni Hacmi için         6

    Çıkış                   7

Lütfen hangi işlmeini yapmak istiyorsanız karşısındaki sayıyı seçiniz.
""")
    try:
        islem = int(input("İşlem tercihiniz: "))
        if islem > 7 or islem < 1:
            print("Lütfen 1 ile 7 arasında değer giriniz.")
            continue
        elif islem == 7:
            break
        elif islem == 1:
            print("""
Karenin alanını seçtiniz.
Bir kenar uzunluğunu giriniz: 
""")
            kenar = int(input("Kenar: "))
            if kenar <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            print("Karenin alanı: ", kenar ** 2)
        elif islem == 2:
            print("""
Üçgenin alanını seçtiniz.
Taban kenar uzunluğunu ve yüksekliğini giriniz: 
""")
            taban_kenar = int(input("Taban Kenar: "))
            if taban_kenar <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            yukseklik = int(input("Yükseklik: "))
            if yukseklik <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            print("Üçgenin alanı: ", (taban_kenar * yukseklik) / 2)
        elif islem == 3:
            print("""
Dikdörtgenin alanını seçtiniz.
İki kenar uzunluğunu giriniz: 
""")
            kenar_1 = int(input("1. Kenar: "))
            if kenar_1 <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            kenar_2 = int(input("2. Kenar: "))
            if kenar_2 <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            print("Dikdörtgenin alanı: ", kenar_1 * kenar_2)
        elif islem == 4:
            print("""
Küpün hacmini seçtiniz.
Bir kenar uzunluğunu giriniz: 
""")
            kenar = int(input("Kenar: "))
            if kenar <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            print("Küpün hacmi: ", kenar ** 3)
        elif islem == 5:
            print("""
Kürenin hacmini seçtiniz.
Yarıçap uzunluğunu giriniz: 
""")
            yaricap = int(input("Yarı çap: "))
            if yaricap <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            print("Kürenin hacmi: ", (4 / 3) * 3.14 * (yaricap ** 3))
        elif islem == 6:
            print("""
Koninin hacmini seçtiniz.
Yarıçap ve yükseklik uzunluklarını giriniz: 
""")
            yaricap = int(input("Yarı çap: "))
            if yaricap <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            yukseklik = int(input("Yükseklik: "))
            if yukseklik <= 0:
                print("Lütfen sıfırdan büyük değerler giriniz.")
                continue
            print("Koninin hacmi: ", (1 /3) * 3.14 * (yaricap ** 2) * yukseklik)
    except:
        print("Lütfen sayısal veriler giriniz.")
        
