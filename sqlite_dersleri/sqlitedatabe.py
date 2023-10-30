#Sqlite Veritabani Tablo Oluşturma
#sütün ve satirlarda verileri toplar 
#örnek 
#ad , soyad, numara    (sütün)
#süheyla,kenet,952     (satirdaki bilgiler)
#sqlite databe internetsiz çalışır.


import sqlite3 
con = sqlite3.connect("dersler.db")     # database oluşturuldu 

cursor = con.cursor()

def tabloolustur():
    cursor.execute ("CREATE TABLE İF NOT EXİST  öğrenciler(ad TEXT ,soyad TEXT,numara İNT ,öğrenci notu İNT )")
    con.commit()
    
def degerekle():
    cursor.execute(" İNSERT İNTO  öğrenciler VALUES ('MUSTAFA','ÇOŞKUN','952','100')")
    con.commit()
    con.close()

tabloolustur()
degerekle()
    
#tabloya dökmedi    Python Dersleri 31 - Sqlite Veritabanı Tablo Oluşturma
