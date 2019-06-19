import vectorOperations
import matrixOperations

#método de GAUSS FUMADO
def gauss(matrix):#escalonamento de matriz pelo método de gauss jordan
    contador=0
    for i in range(len(matrix)-1):
        pivo=matrix[i][i]
        if(pivo!=0):
            for j in range(1+i,len(matrix)):
                k=matrix[j][i]/pivo
                aux=vectorOperations.mult_vector(matrix[i],k)
                aux=vectorOperations.mult_vector(aux,-1)
                aux2=vectorOperations.sum_vector(aux,matrix[j])
                matrix[j]=aux2
            continue
        else:
            contador=1
            #inversão de linhas
            aux=matrix[i]
            matrix[i]=matrix[i+contador]
            matrix[i+contador]=aux
            pivo=matrix[i][i]
            if(pivo==0):
                contador+=1
                #inversão de linhas
                aux=matrix[i]
                matrix[i]=matrix[i+contador]
                matrix[i+contador]=aux
                pivo=matrix[i][i]
                continue
            for j in range(1+i,len(matrix)):
                k=matrix[j][i]/pivo
                aux=vectorOperations.mult_vector(matrix[i],k)
                aux=vectorOperations.mult_vector(aux,-1)
                aux2=vectorOperations.sum_vector(aux,matrix[j])
                matrix[j]=aux2
    return matrix
