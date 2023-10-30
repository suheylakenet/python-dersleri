#Dosyalarda değişiklik yapmak 
"""with open ("yazilim.txt","a") as  dosya :          a= dosyada değişiklik yapmayi sağlar 
    
    dosya.write("melih:kilinc")    """     #yazilim.txt dosyasinda malih kilinç yazisini sona ekledik. 

with open ("yazilim.txt","r+") as dosya :     #r+, bize hem yazma hem okuma imkani sağladi bunu dosyanin en başina yazi ekleyebilmek için kulandik
    data= dosya.read()      #data diye bir dosya tanımlayip dosyayi okttuk yazilimçtxt dosyasi artik datanin içinde
    dosya.seek(0)           #dosyanin en başina seek yardimiyla gittik                
    data="halit: kenet\n" + data  # eklemeyi yaptik 
    dosya. write(data)        #yazdirdik 

"""yukardaki işlem ile dosyanin en başina yazzdirdik """




