#DOSYA AÇMAK VE YAZMAK 
dosya= open("yazilim.txt","w")        
"""'r'	open for reading (defaul)   
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists(olan bir dosyada değişiklik sağlar,DOSYAYA EKLEME YAPAR )
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)"""

dosya.write("NABER")               #W KOMUTU İLE DOSYAYI AÇMIŞTIK. 11.KOD İLE DE AÇILAN DOSYADA NABERİ YAZDIRDIK 