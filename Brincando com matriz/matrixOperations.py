import geradorMatriz
def matrixSum(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def mult_scalar(matriz, escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult

def prodMatrix(matrizA, matrizB):
    """Multiplica duas matrizes."""
    sizeLA = len(matrizA)
    sizeCA = len(matrizA[0]) # deve ser igual a sizeLB para ser possível multiplicar as matrizes
    sizeCB = len(matrizB[0])
    matrizR = []
    # Multiplica
    for i in range(sizeLA):
        matrizR.append([])
        for j in range(sizeCB):
            val = 0
            for k in range(sizeCA):
                    val += matrizA[i][k]*matrizB[k][j]
            matrizR[i].append(val)
    return matrizR
