#Fonksiyonlarda Recursion 
# 1.bitiş durumu tanıımlamak gerekli fonksiyonun sonsuza kadar kendini çağırmaması için 
#2. fonksiyon belli şartlarda kendini çağırması gerek 

""""def topla (liste):
    toplam = 0

    for i in liste:
        toplam += i 
    return toplam 

print(topla([1,2,3,4]))"""""


 
def topla(liste):
    if len(liste)==0:
        return 0
    else:
        return liste [0]+ (topla(liste[1:]))
    
print(topla([1,2,3,4]))
                                                      #alttaki formül recursion  
                                                      #Python3 Dersleri 20 - Fonksiyonlarda Recursion
                                                      