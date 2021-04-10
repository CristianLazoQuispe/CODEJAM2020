import sys
import numpy as np 

T = int(input())

def get_cheater(matriz):
    '''
    #return 50
    i_max = 10000
    maxi = 0
    maxi_ant = None
    for idx,i in enumerate(matriz):
        maxi = max(maxi,sum(i))
        if maxi != maxi_ant:
            i_max = idx
        maxi_ant = maxi
        #i_max = min(i_max,)
    return 1+i_max
    '''
    return 1+ np.argmax(np.sum(matriz, axis=1))

    #return 59

for j in range(T):
    P = int(input())
    matriz1 = []
    matriz = []
    
    #'''
    for i in range(100):
        texto = sys.stdin.readline().strip()#input().strip()#input()
        #print(len(lista))
        matriz1.append(texto)
    for texto in matriz1:
        lista = list(map(int,list(texto)))
        matriz.append(lista)
    
    matriz = np.array(matriz)
    
    print(np.sum(matriz, axis=1))
    #print(np.argmax(np.sum(matriz, axis=1)))
    ans = get_cheater(matriz)

    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            
            