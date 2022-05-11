import random

from random import randint

x = randint(0,100000)
print(x)

def jagamine(arv1,arv2):
    if(arv1 == 0):
        return(arv1,arv2)
    if(arv2 == 0):
        return("SA EI SAA NULLIGA JAGADA")
    else:
        return arv1 / arv2
try:
    x = float(input("Sisesta arv: "))
    y = float(input("Sisesta arv: "))

    print(jagamine(x,y))
except ValueError:
    print("Ei leitud numbrit")



    
