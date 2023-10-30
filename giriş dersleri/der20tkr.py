#ders 20 tekrar kendim yazıyım                     
def geometrik (şekil):
    if len(şekil)==3:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]

        if(a+b>c) and (a+c>b) and(c+b>a):
            if (a==b) and (b==c) and (c==a):
                print("EŞKENAR ÜÇGEN")
            elif (a==b) and ( a==c):
                print("İKİZKENAR ÜÇGEN")

            else:
                print("ÇEŞİTKENAR ÜÇGEN")

    

    
    
    elif len(şekil)==4:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]
        d=şekil[3]

        if (a==b) and (b==c) and (c==d):
            print("KARE")
        elif( a==b) and (c==d):
            print("DİKDÖRTGEN")
        else:
            print("NORMAL DÖRTGEN")




    else:
        print("HERHANGİ BİR ŞEKİL DEĞİL")

    

while (True) :
    elemansayisi = int(input("ELAMAN SAYİSİNİ GİRİNİZ:"))
    if elemansayisi == 3:
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometrik([a,b,c])

    elif elemansayisi==4:
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        geometrik([a,b,c,d])

