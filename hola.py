
lista = [1,2,3,4,5,6,7,8,9]
import random
a=random.choice(lista)
b=random.choice(lista)
c=random.choice(lista)
d=a+b+c
print(a,b,c,d)

def function (a,b,c):
    return a+b+c
d= function(random.choice(lista),random.choice(lista),random.choice(lista))
print(d)

