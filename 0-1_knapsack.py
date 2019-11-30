import time

# funcao que retorna o valor do peso maximo da mochila
def knapSack(W, wt, val, n): 
 
	# caso base
	if n == 0 or W == 0 : 
		return 0

	# verifica o peso do enesimo item.
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 

	else: 
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
				knapSack(W, wt, val, n-1)) 

# vetores
val = [60, 90, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val)

# tempo
inicio = time.time() 

# print do valor do KnapSack
print('KnapSack: ', knapSack(W, wt, val, n))

fim = time.time()

print('Tempo de Execucao: ', fim - inicio)
print('\n')

# source: https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
