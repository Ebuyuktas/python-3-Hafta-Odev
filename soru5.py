#3. Hafta 5. Soru
#Aralýk Yazdýrma Programý
for i in range(1, 101):
    if i % 15 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
