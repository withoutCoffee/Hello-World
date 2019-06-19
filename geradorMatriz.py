from random import randint
#Módulo de cração de matrizes
def createMatrix(lines,columns,n1,n2):#gerar matriz de números aléatório inteiros -10,10
    matrix=[]
    for i in range(lines):
        line=[]
        for j in range(columns):
            line.append(randint(n1,n2))
        matrix.append(line)
    return matrix

def addLines(matrix,line):#inserir linha em matriz
    saida=matrix
    linesMatrix=len(matrix[0])#conta quantos elementos tem em uma linha, conta colunas
    if(len(line)==linesMatrix):
        saida.append(line)
        return saida
    else:
        print("A quantidade de colunas da matriz não é igual a quantidade da linha informada")

def addColumns(matrix,column):#inserir coluna em matriz
    if(len(matrix)==len(column)):
        for i in range(len(matrix)):
            matrix[i].append(column[i][0])
        return matrix
    else:
        print("A quantidade de linhas da matriz não é igual a quantidade da linha informada")
