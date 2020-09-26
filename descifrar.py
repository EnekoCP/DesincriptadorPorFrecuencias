from collections import OrderedDict


hashmap = dict(A= 0, B= 0, C= 0 ,D=0 ,E=0 ,F=0, G=0 ,H=0 ,I=0, J=0 ,K=0 ,L=0 ,M=0 ,N=0, O=0 ,P=0 ,Q=0 ,R=0 ,S=0 ,T=0 ,U=0 ,V=0,W=0, X=0 ,Y=0 ,Z=0)
hashmap_desincripta = dict(A= " ", B= " ", C= " " ,D=" " ,E=" " ,F=" ", G=" " ,H=" " ,I=" ", J=" " ,K=" " ,L=" " ,M=" " ,N=" ", O=" " ,P=" " ,Q=" " ,R=" " ,S=" " ,T=" " ,U=" " ,V=" ",W=" ", X=" " ,Y=" " ,Z=" ")
clave = dict(A= "i", B= "t", C= "l", D= "m", E="b", F= " " , G= " " , H= "q", I= "u", J= "r", K= "n", L= "s", M= " " , N= "h", O= "a", P= "d", Q= "g", R= "p", S= "x", T= " ", U= "o", V= "e", W= " ", X= "c", Y= "f", Z= "j")

def contarFrecuencia(cifrado):

    for i in range(len(cifrado)):
        caracter = cifrado[i]
        if caracter != "." and caracter != "," and caracter != " " and caracter != "(" and caracter != ")":
            hashmap[caracter] = hashmap[caracter]+1

def sustitucion():
    cifrado = "DRCVDVKBOP, VK VC CVKQIOZV PV RJUQJODOXAUK HIV HIVJOAL, IKO ORCAXOXAUK PV VLBVQOKUQJOYAO. PAXNO ORCAXOXAUK PVEV RVJDABAJ UXICBOJ W PVLUXICBOJ VK IKO ADOQVK (VK VC YUJDOBU HIV HIVJOAL) IK DVKLOZV PV BVSBU. "
    lista = list(cifrado)
    contarFrecuencia(cifrado)
    sortedDict = OrderedDict(sorted(hashmap.items(), key=lambda x: x[1] ,reverse=True))
    print(sortedDict)
    chivato = False;
    while chivato==False:
        print("Que letra quieres sustituir?")
        caracterAquitar = input()
        print("Por que letra la quieres sustituir (minuscula) ?")
        caracterAcambiar = input()
        for i in range(len(cifrado)):
            if lista[i] == caracterAquitar:
                lista[i] = caracterAcambiar
                hashmap_desincripta[caracterAquitar]= caracterAcambiar
        cifrado = ''.join(lista)
        print(cifrado)
        print(hashmap_desincripta)
        print("Seguimos? SI O NO")
        respuesta = input()
        if respuesta == "NO" or respuesta == "No" or respuesta == "no" :
            chivato = True

def descifrarDirectamente(cifrado):
    lista = list(cifrado)
    for i in range(len(cifrado)):
        if lista[i] != "." and lista[i] != "," and lista[i] != " " and lista[i] != "(" and lista[i] != ")":
            lista[i] = clave[lista[i]]
    cifrado = ''.join(lista)
    print(cifrado)
descifrarDirectamente("DRCVDVKBOP, VK VC CVKQIOZV PV RJUQJODOXAUK HIV HIVJOAL, IKO ORCAXOXAUK PV VLBVQOKUQJOYAO.")