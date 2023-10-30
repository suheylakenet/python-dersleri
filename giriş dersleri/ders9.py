#KULLANİCİ İSİM VE PAROLA KONTROL PROGRAMI 
# a and b   and bağlacı ikiside doğruysa doğru kabul eder
# a or b    or bağlacı: ya a yada b doğruysa kabul eder
#not a      a normalde doğru olsun ama başına not getirince a yı yanlış kabul eder .

defkullanici="yazilimcibebe"
defparola="1234"

kullanici=input("kullanici adi:")
parola=input("parolaniz:")

if((defkullanici==kullanici) and (defparola==parola)):
    print("hoşgeldiniz")

elif((defkullanici!=kullanici)and (defparola==parola)):
    print("kullanici adini yanliş girdiniz")

elif((defkullanici==kullanici)and (defparola!=parola)):
    print("Şifrenizi mi unuttunuz")

else:
    print("Tekrar deneyiniz")
