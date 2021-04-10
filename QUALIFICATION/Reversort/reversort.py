# python3
# sample test: ok 
# test 1 :  ok
# test 2 : ok

import numpy as np

T = int(input())

def reversort(lista):
    #if len(lista)==1:
    #    return 1
    suma = 0
    for i in range(len(lista)-1):
        j = i+np.argmin(lista[i:])
        #print(i,j,lista,lista[i:j][::-1])
        lista[i:(j+1)] = lista[i:(j+1)][::-1]
        suma += (j-i)
        suma += 1
        
        #print(i,j,j-i+1,lista)
    return suma

for i in range(T):
    N = int(input())
    lista = list(map(int,input().split()))
    #print(lista)
    ans = reversort(lista.copy())
    if i != (T-1):
        print(lista,"Case #"+str(i+1)+": "+str(ans))
    else:
        print(lista,"Case #"+str(i+1)+": "+str(ans))#, end='')
