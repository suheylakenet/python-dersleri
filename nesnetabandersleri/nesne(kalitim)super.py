class EBEVEYN :
    def __init__(self,ad,yas):
        self.ad= ad
        self.yas = yas

    def selamla(self):
        print("merhaba ben",self.ad ,self.yas," 'yasindayim")

class COCUK(EBEVEYN):
    def __init__(self, ad, yas,oyun):
        super().__init__(ad, yas)   #bu super fonksiyonu ile ebeyn sınıfındaki ad ve yaşı içeriye aldık 
        self.oyun = oyun 

    def selamla(self):
       print("merhaba ben ", self.ad ,self.yas,"'yasindayim","en seviğim oyun",self.oyun)


anne= EBEVEYN("AYSE",56)
anne.selamla()

cocuk = COCUK("süheyla",24,"saklambac")
cocuk.selamla()


"""Yukarıdaki örnekte, Ebeveyn adında bir sınıf oluşturduk. Bu sınıf, "ad" ve "yas" adında iki özellik ve "selamla" adında 
bir metot içeriyor. Ardından Cocuk adında bir sınıf oluşturduk ve bu sınıf, Ebeveyn sınıfını miras aldı.

Cocuk sınıfı, Ebeveyn sınıfının özelliklerini ve metotlarını miras
 alırken, selamla metodu için kendi özelleştirmesini yaptı.

Bu sayede, Cocuk sınıfı, hem kendi özelliklerini ve metotlarını 
hem de Ebeveyn sınıfından miras aldığı özellikleri ve metotları kullanabilmektedir. 
Bu, kodun daha modüler ve tekrar kullanılabilir olmasını sağlar."""