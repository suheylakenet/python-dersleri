#NTP - Yapıcı Fonksiyon (init fonksiyonu)2
#__init__() – (başlangıç ve son iki alt çizgili) yapıcı (constructor) olarak bilinen sınıf ilk oluşturulan yapılacak
# işlemlerin tanımlandığı özel bir metottur. 
#Python, bu sınıfın nesne/örnek oluştururken oluştururken çağrılan ilk metottur.
class dusman : 

    def __init__(self,isim,kalan_can,saldiri_gücü,mermi_sayisi):                 #ilk baş bu fonksiyon çağrildi init self ile 
        self.isim= isim
        self.kalan_can=kalan_can
        self.saldiri_gücü =saldiri_gücü
        self.mermi_sayisi= mermi_sayisi


    def print(self):
        print("BASİLİYOR......")
        print("isim:",self.isim,"kalan can:",self.kalan_can,"Saldiri gücü:",self.saldiri_gücü,"mermi sayisi:",self.mermi_sayisi)


dusman1= dusman("ali",50,800,1000)
dusman2= dusman("veli",40,950,520)
print("düşman1.............................................")
dusman1.print()

print("düşman2...............................................")

dusman2.print()

