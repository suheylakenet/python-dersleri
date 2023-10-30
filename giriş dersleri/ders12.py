# FOR DÖNGÜSÜ
string = "gollum"                          #stringte yazdığım kelimeyi tek tek harf harf yazdırdı 
for i in string :
    print(i)
      

liste = ["elma","armut","karpuz"]
for i in liste :
    print(i)            


print(*range(10))                  #0 dan başlayarak 10 a kadar yazdırdı 
print(*range(2,10))                #2den başyarak ona kadar geldi
print(*range(2,10,3))              #2den başlayarak 10 a kadar 3 atlayrak geldi 
 
for i in range(10):                #0dan 10a kadar yazdırdı
    print(i)


for i in range(5,10):                #5den 10a kadar yazdırdı
    print(i)

for i in range(5,10):                #5dan 10a kadar yıldız şekllinde  yazdırdı
    print(i * "*")              
