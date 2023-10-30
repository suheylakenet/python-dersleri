# Dosyalardan Veri Almak 2
#DOSYANİN BELİRLİ BİR YERİNDEN ALMAK 

with open ("yazilim.txt","r") as dosya:            #("yazilim.text","r")= dosya oldu 
    print(dosya.read())
    dosya.seek(5)                        #yazilim.txt dosyasında 5. karakterden sonrasini çağirdi
    print(dosya.read())


    dosya.seek(5)                        
    print(dosya.read(4))            #5.karakterden başlayıp 4 karakter ileri gitti