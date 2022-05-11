
n = int(5)

nn = int(55)

nnn = int(555)

arv = n
arv2 = nn
arv3 = nnn


def liitmine():
    print(arv+arv2+arv3)
liitmine()


a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
