#İNPUT FONKSİYONU VE FORMAT FONKSİYONU 
a=input()      #kullanıcıdan bilgi aldı ve yazdırdı 
print(a)

a=input("bir sayi girin:")
print(a)                      #bir sayı girin diye yazdırması gerekiyodu yazdırmadı 

a=input("birinci sayi")
b=input("ikinci sayi")
c=input("üçüncü sayi")

print("sayilarin toplami:",a+b+c) #bu şekilde cevap abc şekilde yanlış çıkıyo, doğru toplayabilmesi için aşağıdaki ile int e çevrilir 
print("sayilarin toplami:",int(a)+int(b)+int(c))
