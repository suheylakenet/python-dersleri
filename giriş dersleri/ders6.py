#İNPUT FONKSİYONLARI DERSE DEVAM 2              *FORMAT FONKSİYONU*
print("oyuncu kaydetme prograrami:")
ad=input("Oyuncunun adi:")
soyad=input("Oyuncun soyadi:")
takim=input("Oyuncunun takimi:")

bilgiler=[ad,soyad,takim] 

print("data base kaydediliyor....")

print("Oyuncunun adi:{},Oyuncun soyadi:{},Oyuncunun takimi:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Kaydedildi....")



# /n  fonksiyonu ne işe yarıyor anlaşılsın diye 
print("oyuncu kaydetme prograrami:")
ad=input("Oyuncunun adi:")
soyad=input("Oyuncun soyadi:")
takim=input("Oyuncunun takimi:")

bilgiler=[ad,soyad,takim] 

print("data base kaydediliyor....")       #\n çalışmadı 
                                             
print("Oyuncunun adi:{}\nOyuncun soyadi:{}\nOyuncunun takimi:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Kaydedildi....")