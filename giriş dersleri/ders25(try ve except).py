#TRY VE EXCEPT                        olabilcek çıkabilcek hataları sisteme kendimimiz gireriz. try le çıkabilcek hataları düzeltiriz.
sayi1= input("SAYİ1:")                # except ile çıkabilcek hataları sisteme kendimiz gireriz . artık o hata oluştuğuda sistem eror
sayi2= input("SAYİ2:")                # vermezz kendisi hangi hata olduğunu söyler 

try:
    sayi1= int(sayi1)
    sayi2= int(sayi2)
    print(sayi1/ sayi2)
          

except ValueError:
    print("lütfen 10luk tabaninda bir sayi giriniz")

except ZeroDivisionError :
    print("bir sayi sifira bölünemez")


#except (ValueError, ZeroDivisionError):             ""buda bir seçenektir. 
    #print("bir hata oluştu")                
