try:
    dosya = open("yazilimbilimi.txt","r")

except IOError:
    print("DOSYA BULUNAMADİ")

finally:
    dosya.close