#ders 23.2 devam 
#ÖRNEK
dersler={"süheyla":["süt","et"] ,"onur":["python","lab"]}

isim=input("isim giriniz:")

print("{}in aldiği dersler:".format(isim))
for i in (dersler[isim]):
    print(i)