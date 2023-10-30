#Inheritance (Kalıtım)  #OVERRİDDİNG      +super fonksiyonu 
class calişan ():    #kalitim konusunda iki nokta böyle atilir
    def __init__(self,isim,maas,departman):
        print("çalişan sinifinin yapici fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("çalişan sinifin bilgileri gösteriliyor...")
        print("isim",self.isim,"maaş",self.maas,"çaliştiği departman",self.departman)

    def maasazamyap (self,zam_miktari):
        print("maaşa zam yapildi") 
        self.maas +=zam_miktari
    def departmandegiştir(self,yeni_departman):
        print("departman değiştiriliyor......")
        self.departman = yeni_departman


class yönetici (calişan):     #kalıtım yaptık.artık yönetici bütün çalışan fonksiyonlarına sahip
    def __init__(self, isim, maas, departman,kisi_sayisi):
        print("Yönetici sinifin yapici fonksiyonu")
        super().__init__(isim,maas,departman)   #yukardaki isimmaas departmanı tek tek self.yazmadan çekniş olduk 
        self.kisi_sayisi= kisi_sayisi   #ek özellik 
        super().bilgilerigoster
        

   

Yönetici =yönetici("mehmet",2500,"ik",20)


        