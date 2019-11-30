import random
import time

taken = [[0 for x in range(100) for y in range(100)]]

def knapsack(pesoLim, pesos, valores, n):

    global taken
    i = 0
    w = 0
    K = [[0 for x in range(1000) for y in range(1000)]]
    while(i<n):
        while(w<pesoLim):
            if(i==0 or w==0):
                K[i][w] = 0
            elif(pesos[i-1] <= w):
                K[i][w] = max((valores[i-1] + K[i-1][w-pesos[i-1]]), (K[i-1][w]))
                if(K[i][w]==valores[i-1] + K[i-1][w-pesos[i-1]]):
                    taken[i][w] = True
            else:
                K[i][w] = K[i-1][w]
            w+=1
        i+=1

    print("Valor da mochila = ")
    print (K[n][pesoLim])
    res = K[n][pesoLim]
    w = pesoLim    
    i = n

    while(i>0 and res>0):
        if(res == K[i - 1][w]):
            continue
        else:
            print("valor do item = ", valores[i-1])
            print("Peso = ", pesos[i-1])
            res = res - valores[i-1]
            w = w - pesos[i-1]
        i-=1

valores = []
pesos = []

print("Informe o tamanho dos vetores: ")
size = int(input())

if(size<100):
    i=0
    while(i<size):
        valores.append(random.randint(0,1000))
        i+=1

if(size < 20):
    print(valores)


if(size<100):
    i=0
    while(i<size):
        pesos.append(random.randint(0,100))
        i+=1

if(size < 20):
    print(pesos)

print("Insira o peso máximo da mochila: ")
pesoLim = int(input())

n = len(valores)

inicio = time.time()

knapsack(pesoLim, pesos, valores, n)

fim = time.time()

print('Tempo de Execucao: ', fim - inicio)
