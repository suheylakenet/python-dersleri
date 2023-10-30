# FOR DÖNGÜSÜ ÖRNEK PROGRAM 

faktoriyel = 1                                                     #BAŞARISIZ 

while True:
    faktoriyel = 1
    sayi=int(input("faktoriyelini almak istediğiniz sayiyi giriniz:"))
    if sayi <=0:
        print("lütfen negatif  ve 0 olmayan sayi giriniz")
    else:
        for i in range (1,sayi +1):
            faktoriyel *=i
            print("Faktoriyel",faktoriyel)
            break

        