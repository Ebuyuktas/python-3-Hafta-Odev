#3. Hafta 3. Soru
#Futbolcu Ayıklama Programı
try:
    futbolcular = open("futbolcular.txt", "r")
    futbolcu_isimleri = futbolcular.readlines()
    fener = open("fenerbahçe.txt", "w")
    gs = open("galatasaray.txt", "w")
    bsk = open("beşiktaş.txt", "w")
    for futbolcu in futbolcu_isimleri:
        if "Fenerbahçe" in futbolcu:
            fener.write(futbolcu)
        elif "Galatasaray" in futbolcu:
            gs.write(futbolcu)
        elif "Beşiktaş" in futbolcu:
            bsk.write(futbolcu)
    fener.close()
    gs.close()
    bsk.close()
    futbolcular.close()
    print("Futbolcular ilgili dosyalara transfer edildi.")
except:
    print("Dosya açarken hata oluştu ya da bulunamadı") 
