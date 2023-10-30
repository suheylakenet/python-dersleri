#LİSTELER 
a=(23,37,40,"python",3.12)      #bir küme açıkladım ve yazdırdım 
print(a)
oyuncu=list(("arda","turan",28,1.78))
print(oyuncu)
print(oyuncu[0])                #oyuncu kümesinin ilk elamınını yazdırdı 
print(oyuncu[1])                #oyuncu kümesinin ikinci elamınını yazdırdı 
oyuncu[1]="URAN"                #kümede değişiklik yapılmak isterse, değişkenlerden ikinci olanı değiştirdik
print(oyuncu)
oyuncu.append("barcelona")       #append ile kümeye ekleme yapıldı 
print(oyuncu)

print(oyuncu +["atletico madrid"]) # bu şekilde de kümenin yanına ekleme yapılabilir 
oyuncu=oyuncu+ ["atletico madrid"] #bu şekilde de eklenebilir 
print(oyuncu)

print(oyuncu[:2])                  #en baştan ilk ikiyi yazdırdı 
oyuncu[:2]=["süheyla","kenet"]     #en baştan ilk ikiyi bu şekilde değiştirdik
print(oyuncu)

oyuncu[:2]=[]                      #ilk iki haneyi boş bıraktı 
print(oyuncu)

oyuncu[:]=[]                      #tüm kümeyi boş bıraktık 
print(oyuncu)