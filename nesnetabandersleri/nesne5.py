# NTP - Düşman Sınıfını Geliştirmek 2 (Ek olarak bir duyuru)
import random
class dusman : 

    def __init__(self,  isim="düşman", kalan_can=500, saldiri_gücü= 10, mermi_sayisi=5):            #ilk baş bu fonksiyon çağrildi init self ile 
        self.isim= isim
        self.kalan_can=kalan_can
        self.saldiri_gücü =saldiri_gücü
        self.mermi_sayisi= mermi_sayisi

    def saldir(self):
        print(self.isim + "SALDİRİYOR.")
        harcanan_mermi =random.randrange(0,10)
        print(str(harcanan_mermi)+ "kadar harcandi")
        self.mermi_sayisi -= harcanan_mermi

    def saldiriya_ugra(self,harcanan_mermi, saldiri_gücü):
        print("vuruldum")
        kalancan -=(harcanan_mermi +saldiri_gücü)

    def mermi_bitti_mi(self):
        if(self.mermi_sayisi<=0 ):
            print(self.isim + "konusuyor: MERMİ BİTTİ OYUNDAN ÇİKİYORUM")
            return True
        return False
    

    def hayatta_mi(self):
        if(self.kalan_can<=0):
            print("ÖLÜYORUMMMMM.......")




    def print(self):
        print("BASİLİYOR......")
        print("isim:",self.isim,"kalan can:",self.kalan_can,"Saldiri gücü:",self.saldiri_gücü,"mermi sayisi:",self.mermi_sayisi)

dusmanlar =  []


i=0 
while ( i <10) :
    rastgelecan=random.randrange(100,200)
    rastgelesaldirigücü=random.randrange(10,20)
    rastgelemermi= random.randrange(20,30)
    yenidüşman= dusman("dusman"+str(i+1),rastgelecan,rastgelesaldirigücü,rastgelemermi)
    dusmanlar.append(yenidüşman)

    i += 1

i= 0
while (i<3):
    randomdusman1= random.randrange(0,10)
    randomdusman2= random.randrange(0,10)


    donendeger= dusmanlar[randomdusman1].saldir()


    dusmanlar[randomdusman2].saldiriya_ugra (donendeger[0] ,donendeger[1])


    print("RAOUND BİTTİ .....")

    i+=1 
