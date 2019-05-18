from random import randint
def createVector(columns,n1,n2):#gerar vetor de números aléatório inteiros -n1 até n2
    vector=[]
    for i in range(columns):
        vector.append(randint(n1,n2))
    return vector

def mult_vector(lista,escalar):
    saida=[]
    for i in range(len(lista)):
        saida.append(lista[i]*escalar)
    return saida
def sum_vector(v1,v2):
    if(len(v1)==len(v2)):
        saida=[]
        for i in range(len(v1)):
            saida.append(v1[i]+v2[i])
        return saida
    else:
        print("lista de tamanhos diferentes")
