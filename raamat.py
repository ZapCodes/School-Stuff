raamatud = {"RAAMAT":'',"AUTOR":'',"ISBN":''}


def lisama():
    
    while len(raamatud) + 6:
        raamat = input("Sisesta raamat:")
        raamatud.update({"RAAMAT":raamat})
        
        print("Lisasite korvi raamatu",[raamat])
        print(raamatud)
    
        menu()
        
def autor():
    autor = input("Sisesta autor: ")
    raamatud.update({"AUTOR":autor})
    print("Lisasite autoriks: ",[autor])
    print(raamatud)
    menu()

def korvis(raamatud): 
    key_list = list(raamatud.keys())
    print(raamatud)
    menu()


def kustutama():
    
    while True:
        kasutaja = input("Sisestage '-' et tühistada valikud: ")
        if kasutaja == '-':
            raamatud.clear()
            print("Taastamine")
            raamatud.update({"RAAMAT":'',"AUTOR":'',"ISBN":''})
            print("Kustutamine edukas!")
            menu()
        else:
            print("Nah")    

def isbn():
    while True:
        isbn = input("Sisesta ISBN kood: ")
        if len(isbn) == 13:
            raamatud.update({"ISBN":isbn})
            print(raamatud)
        elif len(isbn) > 13:
            print("Sisestasite liiga suurelt!!!")
            print("ISBN peab olema 13 numbrit :)")
        elif len(isbn) < 13:
            print("Sisestasite liiga väikselt!!!")
            print("ISBN peab olema 13 numbrit :)")   
        else:
            print("Te ei sisestanud koodi")
        menu()


def menu():
    print("""

    1.Sisesta Raamat
    2.Sisesta Autor
    3.Märksõna abiga
    4.Korvis
    5.ISBN
    6.Eemalda korvist
    
    """)

    kasutaja = input("Sisesta valikud:")
    
    while True:
        if kasutaja == '1':
            lisama()
            menu() 
        elif kasutaja == '2':
            autor()   
        elif kasutaja == '3':
            #märksõna()
            menu()
        elif kasutaja == '4':
            korvis(raamatud)
        elif kasutaja == '5':
            isbn()
        elif kasutaja == '6':
            kustutama()
        else:
            print("Valige vähemalt 1 valikutest")
menu()        

#def märksõna():
    
   # kasutaja = input("Sisesta raamatu märksõna: ")
   # print(raamatud.keyword.kwlist)
   # menu()


    
             

