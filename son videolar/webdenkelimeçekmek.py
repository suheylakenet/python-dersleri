#Bir Web Sitesindeki Kelime Frekansı 1 ( İnternetten Veri Çekmek)
import requests
from bs4 import BeautifulSoup

url="https://www.ntv.com.tr/turkiye/prof-dr-aziz-sancar-kimdirnobel-odulu-kazanan-ilk-turk-bilim-insani-olmustu,sAtrqnWao0636sNSktWTSw"


tümkelimeler = []

r= requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

for kelimegruplari in soup.find_all("p"):
    print("kelimegruplari")