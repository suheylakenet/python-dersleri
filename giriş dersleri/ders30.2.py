#Dosyalarda değişiklik yapmak 2
#dosyanin ortasinda değişiklik yapmak için ne yapılır 

liste=[1,2,3,4,5]
liste.insert(1,15)    #listede 1 in yanina eklemek için yaptık 
print (liste)

"""liste=[9,8,7,6]  
liste.insert(8,56)        # bu kod sona ekledi ortasina eklemk için çalişmadi 
print(liste)       """""  

#dosyanin ortalarina yerleştirmek için uygulama 
with open ("yazilim.txt","r+") as dosya :
    data= dosya.readlines() 
    data.insert(1,"masa:saat\n")
    dosya.seek(0)
    dosya.writelines(data)            # bu şekilde dosyada 1.satirimdan sonraya ekleme yaptık 