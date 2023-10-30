#KOŞULLU DURUMLAR (if,elif,else)
yaş=int(input("yaşinizi giriniz:"))    #Yaşinizi girniz cümlesi str olduğundan onu int e çevirdik 


if yaş>= 18:
    print("Mekana girebilirsiniz")

else:                                #else, if in çalışmadığı durumlarda geçerlidir 
    print("mekana giremezsiniz")


