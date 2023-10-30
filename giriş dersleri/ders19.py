#fonksiyonlarda varsayilan değerler 
def kayit_ekle (ad="bilgi yok",soyad="bilgi yok",yaş="bilgi yok",meslek="bilgi yok"):
    print("Kayit eklelniyor")

    print("ad:{}\nsoyad:{}\nyaş:{}\nmeslek:{}".format(ad,soyad,yaş,meslek))
    print("kayit başariyla eklendi")
    
    
    
#kayit_ekle("onur","bostaci")    def kayıt ekledeki ilk ikisi ne ise onu yazdırdı mesela girişe onur 25 yazsaydik çıktı da soyad 25 gözükcekti ve yanlış olcaktı 
kayit_ekle(ad="onur",yaş=25)     
