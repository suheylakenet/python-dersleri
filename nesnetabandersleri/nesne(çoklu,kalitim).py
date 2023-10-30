#ÇOKLU KALİTİM 
class Asker:
    def ates_et(self):
        print("Ateş ediyorum!")

class Pilot:
    def uc(self):
        print("Uçuyorum!")

class PilotAsker(Asker, Pilot):
    def komut_ver(self):
        print("Komut veriyorum!")

# PilotAsker sınıfı, Asker ve Pilot sınıflarından miras aldı.
pilot_asker = PilotAsker()

pilot_asker.ates_et()  # Asker sınıfından miras aldığı metodu çağırır.
pilot_asker.uc()       # Pilot sınıfından miras aldığı metodu çağırır.
pilot_asker.komut_ver()  # Kendi sınıfına ait metodu çağırır.

#Bu örnek, birden fazla üst sınıfın özelliklerini ve davranışlarını
#  tek bir alt sınıfta birleştirerek çoklu kalıtımın nasıl çalıştığını göstermektedir.