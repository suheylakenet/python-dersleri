print("Suhom")


faktoriyel =1 
while True:
    faktoriyel = 1
    sayi = int(input("Faktoriyelini bulmak istediğiniz sayıyı giriniz:"))
    if sayi <= 0 :
        print("Lütfen 0 ve negatif olmayan bir sayı giriniz.")
    else:
        for i in range(1,sayi+1):
            faktoriyel *= i
         print("Faktoriyel",faktoriyel)
        break