#Dosyadan Veri Almak,Okuma İşlemleri 

dosya = open ("yazilim.txt","r")
""""
read()        #bütün dosyanin içinde ne varsa alinmasini sağlar ve yazdirir.
readline()    #dosyanin içindeki ilk satiri alir ve yazdirir (süheylakeneti yazdırdı)
              #eğer alt alta üç tane print(dosya.readline()) yazilsaydi dosyaizdaki 3 saatiri da alirdi.


readlines()    # tüm dosyayi yazdirir fakat liste şeklinde yazdirir yani yan yana yazdirir.

dosya = open ("yazilim.txt","r")
liste= dosya.readlines()
print(liste[1])                  #bu yalnizca ilk satiri yazdirmasini sağlar 


dosya.close()              #dosyayi kapatir




"""""          

print(dosya.readlines())
