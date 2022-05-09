def liitmine(arv,arv2):
    return(arv + arv2)
def lahutamine(arv,arv2):
    return(arv - arv2)
def korrutamine(arv,arv2):
    return(arv * arv2)
def jagamine(arv,arv2):
    return(arv / arv2)

print("LIITMINE, LAHUTAMINE, KORRUTAMINE, JAGAMINE")

arvutamine = input("Sisestage enda valik: ")

if(arvutamine == 'LIITMINE'):
    Vastus1 = liitmine(int(input("Sisesta arv: ")),int(input("Sisesta arv 2: ")))
    
    print(Vastus1)
elif(arvutamine == 'LAHUTAMINE'):
    Vastus2 = lahutamine(int(input("Sisestage arv: ")),int(input("Sisestage arv 2: ")))
    print(Vastus2)
elif(arvutamine == 'KORRUTAMINE'):
    Vastus3 = korrutamine(int(input("Sisestage arv: ")),int(input("Sisestage arv 2: ")))
    print(Vastus3)
elif(arvutamine == 'JAGAMINE'):
    Vastus4 = jagamine(int(input("Sisestage arv: ")),int(input("Sisestage arv 2: ")))
    print(Vastus4)
else:
    print("TE EI VALIINUD ÕIGET LAHENDUST!!")