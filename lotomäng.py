## VALIN 9 NUMBRIT

## LISAN FUNKTSIOONI NUMBRID 1- 99

## LOTO ENNUSTAB SUVALISED NUMBRID VAHEMIKUS 1-99 MIDA TA TEEB 9 KORDA

## KUI KÕIK NUMBRID ON ÕIGED SIIS ON VÕIT

#  KUI 4 ÕIGET ON VÕIT 200€

# KUI 5 ÕIGET ON VÕIT 1000€

# KUI 6 ÕIGET ON VÕIT 3000€

# KUI 7 ÜIGET ON VÕIT 5000€

# KUI 8 ÕIGET ON VÕIT 10000€



from random import randint

# loon kasutajale numbrite kogumi kuhu need salvestuvad
kasutajanumbrid = list()
masinanumbrid = list()



# funktsioon valimiseks
def kasutajavalik():
    # kasutan for et tegevus korduks 9 korda
    for i in range(9):
        while True:
            # suurendan 1 väärtust iga tsükli võrra 1 võrra
           
            arvud = int(input(f"Vali {i+1} suvaline number: "))
                
            if arvud in range(1,100):
                if arvud in kasutajanumbrid:
                    print("See number on juba valitud")
                else:
                    kasutajanumbrid.append(arvud)
                    break           
    return kasutajanumbrid    
kasutajavalik()    

for item in kasutajanumbrid():
    print(item)

def lotomasin(arg1):
    if arg1 == 'Y':

        y = masinanumbrid

    else:
        y = kasutajanumbrid

    for i in range(9):

        x = randint(1,100)

        while True:
            if x in range(1,100):

                if x in y:

                    print("Selline number on juba olemas või valitud")
                else:

                    masinanumbrid.append(x)
                    break
    return masinanumbrid

for item in lotomasin():

    print(masinanumbrid) 

def numbri_kontroll():
    aa = set(kasutajanumbrid)
    print(aa.difference())

def loto_system():

    kasutajanumbrid.clear()
    masinanumbrid.clear()
    kasutajavalik()
    lotomasin()
    

loto_system()




