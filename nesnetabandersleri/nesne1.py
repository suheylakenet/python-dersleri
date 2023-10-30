#Sınıflar ve Nesneler (Nesne Tabanlı Programlama) 

class dusman:
    kalan_can=3
    def __init__(self):               #self= claas içindeki diğer fonksiyonlarda da geçerli kılar. 
        self.x = 5 
        self.name ="Suheyla"
        print(self.x)
    

    def saldir (self):
        print(self.name)
        print(self.x)
        print("HUCUUUUUUM")
    
        self.kalan_can -=1

    def hayatta_mi(self):
        if (self.kalan_can<= 0):
            print(self.name)
            print("ÖLDÜ")

        else:
            print(str(self.kalan_can) + "canim kaldi")
    def durdur(self):
        self.kalan_can = self.kalan_can
        print("Durduruldu.")


dusman1 = dusman()

dusman1.saldir()
dusman1.hayatta_mi()
dusman1.durdur()


