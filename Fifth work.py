import random
import math
def passeio(n: int):
    x1 = 0
    y1 = 0
    ###1 = pra cima(x1 += 1), 2 = pra baixo(x1 -= 1), 3 = esquerda(y1 -= 1), 4 = direita(y1 += 1)
    print("(0, 0)")
    for i in range(n):
        passo = random.randint(1, 4)
        if passo == 1:
            x1 += 1
        elif passo == 2:
            x1 -= 1
        elif passo == 3:
            y1 -= 1
        elif passo == 4:
            y1 += 1
        print("(" + str(x1) + ", "+ str(y1) + ")")
    #P (px, py) = (0,0) Q (qx, qy) = (x1, y1)
    euclidiana = math.sqrt((0 - x1)**2 + (0 - y1)**2)
    print("distancia = ", euclidiana)

#formatar
passeio(10)    
          
def popular_rede_social_aleatoriamente(P: float, matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j:
                par = random.uniform(0, 1)
                if par < P:
                    matriz[i][j] = 1
                    matriz[j][i] = 1
                else:
                    matriz[i][j] = 0
                    matriz[j][i] = 0
            else:
                matriz[i][i] = 0
                
m = [[0 for j in range(5)] for i in range(5)]
popular_rede_social_aleatoriamente(0.8, m)

def amigos_em_comum(i: int, j: int, matriz: list):
    contadora = 0
    lista = []
    for i2 in range(len(matriz[i])):
        if i != i2 and j != i2:
            if matriz[i][i2] == 1 and matriz[j][i2] == 1:
                contadora += 1
                lista.append(i2)

    return(contadora, lista)

m = [[0 for j in range(5)] for i in range(5)]
popular_rede_social_aleatoriamente(0.8, m)
print(amigos_em_comum(1, 2, m))

def coeficiente_de_aglomeracao(i: int, matriz: list):
    cont = 0
    lista = []
    for i2 in range(len(matriz[i])):
        if matriz[i][i2] == 1:
            lista.append(i2)
    for u in lista:
        for v in lista:
            if u != v:
                if matriz[u][v] == 1:
                    cont += 1

    n = len(lista)
    denominador = n * (n-1) / 2

    return cont / denominador
        

#m = [[0 for j in range(10)] for i in range(10)]
#popular_rede_social_aleatoriamente(0.8, m)
#print(amigos_em_comum(1, 2, m))
#print(coeficiente_de_aglomeracao(2, m))

def picos(terreno: list):
    contadora = 0
    for i in range(len(terreno)):
        for j in range(len(terreno[i])):
            pico = True
            meio = terreno[i][j]
            if i - 1 >= 0:
                if terreno[i - 1][j] >= meio:
                    pico = False
            if i + 1 < len(terreno):
                if terreno[i + 1][j] >= meio:
                    pico = False
            if j - 1 >= 0:
                if terreno[i][j -1] >= meio:
                    pico = False
            if j + 1 < len(terreno[i]):
                if terreno[i][j + 1] >= meio:
                    pico = False
            if pico == True:
                contadora +=1

    return contadora
m = [[1, 3, 4], [2, 5, 7], [2, 8, 3]]
print(picos(m))


