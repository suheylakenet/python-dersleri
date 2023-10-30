# GLOBAL VS LOCAL VARIABLES

""""
Global Variables: Global variable is a variable that is run everywhere in the program. 
-> It runs until the program executed.
-> It is created in the run time process.

Local Variables: Local variable is a variable that is run in a specific place (in C their scope is started with { and end with } ) then it is removed.
-> You can not use that variable out of its scope.
-> It is generally used in functions and if we need that value we can return that variable.


"""

 
 #global variable Tipi int oldugu icin hafizada 4byte lik yer ayirir  1 byte -> 8 bittir Her bit ya sifir yada birdir
a = 25  # 0000 0000 0000 0000 0000 0000 0001 1001  
        # 1 +  0 + 0 + 8 + 16 = 25
a = 18





def some_func():
    b = 12  # local variable 
    global a
    a = 10  # local variable
    result = a+b  # hafizadaki result degiskeninin bulundugu yere 30 yazdirdi
    print(result)



def some_func2(param1,param2):
    result = param1 + param2 + a
    return result




def some_func3(param1,param2):
    global result 
    result = param1 + param2


some_func()
# Hafizafa olusturulan b ve result degiskenlerinin degeri degistirlmiyor, Fakat hafizadaki bu yer program tarafindan serbest birakiliyor
# Daha sonra program ihtiyac duyarsa b ve result degiskenlerinin hafizada bulundugu yere herhangi bir degisken atayabilir.

print("Some_func2 sonucu : ",some_func2(12,12))
some_func3(12,12)
print("Some_func3 sonucu : ", result)

