nimi = input("Teie nimi: ")
#print("TERE" +nimi)
vanus = int (input("Sisestage enda vanus: "))
#number = vanus
#tulemus = ("TE OLETE PIISAVALT VANA")
i = 0
if(vanus > 18):
    for i in range(vanus):
     print("VAU " +nimi)
else:
    print("OMAIGAd " +nimi)