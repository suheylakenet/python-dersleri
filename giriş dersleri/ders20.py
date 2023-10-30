#GEOMETRİK ŞEKİL HESAPLAMA ÖRNEK FONKSİYON 
def geometrik(şekil):
    if len(şekil)==3:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]
      
        if(a+b)>c and (a+c)>b and (b+c)>a :
            if (a==b) and(a==c) and (b==c):
                print("eşkenar üçgen")
            elif(a==b) and (a==c):
                print("ikizkenar üçgen")

            else:
                print("çeşitkenar üçgen")
        else:
            print("üçgen belirtmiyor")

    elif len(şekil)==4:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]
        d=şekil[3]
        if(a==b) and(b==c) and (c==d):
            print("kare") 
        elif(a==c) and (b==d):
            print("dikdörtgen")

        else:
            print("normal dörtgen")


    else:
        print("Herhangi bir şekil değil")

while (True):
    elemanSayisi = int(input("Eleman sayisini giriniz :"))
    if (elemanSayisi == 3):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        geometrik([a,b,c])

    elif(elemanSayisi==4):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))
        geometrik([a,b,c,d])




    else:
        print("Herhangi bir şekil değil")



