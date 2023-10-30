#WHİLE DÖNGÜSÜ ÖRNEK PROGRAM 
#break deyimi = döngünün içinde kullanıldığı zaman döngü sona erer 


defkullanici ="yazilimcibebe"
defparola ="1234"

while (True):
    kullanici= input("kullanici adi:")
    parola = input("parola:")
    if((kullanici==defkullanici)and (parola==defparola)):
        print("Hoşgeldiniz",kullanici)
        break

    elif((kullanici!=defkullanici)and (parola==defparola)):
        print("kullanici adini yanliş girdiniz")
    elif ((kullanici==defkullanici)and (parola!=defparola)):
        print("Şifreni mi unuttunuz? ")
        print("Şifreyi değiştirmek ister misiniz?(E\H)")
        cevap = input()
        if(cevap=="E"):

            yeniparola = input("yeni parola:")
            print("Lütfen bekleyin")
            defparola = yeniparola
            print("şifre başari ile değiştirildi")
    
    else:
        print("Tekrar deneyin")
