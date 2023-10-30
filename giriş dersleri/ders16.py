#kendim örnek çalışma 

print("KELİME EŞLEME PROGRAMI")

while True :
    "black" == ("siyah")
    black= input("black keimesinin türkçesini yaziniz:")
    if (black=="siyah"):
        print("TEBRİKLER DOĞRU CEVAP.")
    else:
        print("yanliş cevap,doğru cevap=siyahtir")

    "white" == ("beyaz")
    white = input(" white kelimesinin türkçesini giriniz.:")
    if(white=="beyaz"):
        print("TEBRİKLER DOĞRU CEVAP.")
    else:
        print("YANLİŞ CEVAP, WHİTE BEYAZ DEMEKTİR.")

    "green"== ("yeşil")
    green= input("green türkçesini yaziniz:")
    if(green== "yeşil"):
        print("tebrikler doğru cevap")
    else:
        print("yanliş cevap green, yeşil demektir")

    "purple"== ("mor")
    purple =input("purple türkçesini yaziniz:")
    if(purple=="mor"):
        print("TEBRİKLER DOĞRU CEVAP ")
    else:
        print("yanliş cevap purple mor demektir")

    x= input("testi tekrar yapmak istiyorsaniz evet yapmak ,yapmak istemiyorsaniz hayir yazin.:")
    if (x==" evet"):
        continue 
    elif (x=="hayir"):
        print("TEBRİKLER TESTİ BİTİRNİZ")
        break                               

