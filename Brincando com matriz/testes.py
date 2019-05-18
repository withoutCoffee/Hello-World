import matrixOperations
import geradorMatriz
import vectorOperations
import gauss
def exibirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(" [",matriz[i][j],end="] ")
        print("")
'''
a=geradorMatriz.createMatrix(3,3,-3,10)
b=geradorMatriz.createMatrix(3,1,-5,10)
'''
#a=[[2,1,1,8],[1,1,4,15],[0,3,2,9]]#matriz para testes
a=[[1,2,1,9],[2,1,-1,3],[3,-1,-2,-4]]#matriz para testes
#a=geradorMatriz.addColumns(a,b)
exibirMatriz(a)
print("")
a=gauss.gauss(a)
exibirMatriz(a)
