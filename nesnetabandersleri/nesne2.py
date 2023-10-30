#NTP - Yapıcı Fonksiyon (init fonksiyonu)
class dusman :
    isim= "düşman"
    kalan_can="1500"
    saldiri_gücü ="300"
    mermi_sayisi="40"
    def print(self):
        print("BASİLİYOR......")
        print("isim:",self.isim,  "kalan can:",self.kalan_can,  "Saldiri gücü:",self.saldiri_gücü,  "mermi sayisi:",self.mermi_sayisi)


dusman1= dusman()
dusman2= dusman()
print("düşman1.............................................")

dusman1.print()


print("düşman2...............................................")

dusman2.print()

