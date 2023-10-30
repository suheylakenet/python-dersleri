#continue kavramı s
listeler =[2,3,4]
for i in range (1,10):
    if (i in listeler ):
        continue
    print(i)                         # ormalde for i in range (1,10) 1,2,3,4,5,6,7,8,9 bastırır biz ona if i in listeler 
                                     # dediğimizde listelerdeki i değerlerini es geçerek devam ettirir yani şu anda yazdırdığı değer 
                                     # 1,5,6,7,8,9 dur.