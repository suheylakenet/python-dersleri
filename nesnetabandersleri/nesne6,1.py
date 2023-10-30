#Inheritance (Kalıtım)  #OVERRİDDİNG
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

"""calişan= calişan("mehmet baltaci",2500,"insan kaynaklari")
calişan.bilgilerigoster() """ 
       #bu şekilde yazdırdı     #çalişan sinifinin yapici fonksiyonu
                                #çalişan sinifin bilgileri gösteriliyor...
                                #isim mehmet baltaci maaş 2500 çaliştiği departman insan kaynaklari     


class yönetici (calişan):     #kalıtım yaptık.artık yönetici bütün çalışan fonksiyonlarına sahip
    def __init__(self, isim, maas, departman,kisi_sayisi):
        #hem yukarıda tanımlı init fonksiyonu var hem burda buna OVERRİDDİNG denir 
        #Yukarda yazilan init fonksiyonunu kullanma kendi yazdığımı kullan dersek bunu kullanırız
        print("Yönetici sinifinin yapici fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi    #EK ÖZELLİK 

#eğer tek tek self. diye classın içine yazmak istemezsek farklı bir özellik var onuda yeni dosyada analtıyım


   

Yönetici =yönetici("mehmet",2500,"ik",20)
Yönetici.bilgilerigoster()

        