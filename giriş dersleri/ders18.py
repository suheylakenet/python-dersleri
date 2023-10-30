#FONKSİYONLARDA RETURN 
def kökbul (a,b,c):
    delta =(b*b-4*a*c)
    if (delta <0):
        print("Reel kök bulunamadi")
        return                      #return fonksiyonu bitirir . kod daha aşağısı çalışmaz . dış dünyaya akatarır . 
    
    x1= (-b-delta**0.5)/(2*a)     
    x2= (-b+delta**0.5)/(2*a)    
    
    return(x1,x2)

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

sonuc=kökbul(a,b,c)
print(sonuc)
