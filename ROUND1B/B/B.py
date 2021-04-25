def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))

m = 1000000007

import numpy as np 

def print_list(lista):
    s=""
    for i in lista[:-1]:
        s+=str(i)+" "
    s+=str(lista[-1])

    return s

def solve2(ns,a,b,metales):
    #print(ns,metales)

    if len(metales)==0:
        return True
    if sum(ns)==0:
        return len(metales)==0

    for n in ns:
        n1 = n-a
        n2 = n-b        
        if n1>0:
            if n1 in metales:                
                metales[n1]-=1
                if metales[n1]==0:
                    del metales[n1]
            else:
                ns.append(n1)                    
        if n2>0:
            if n2 in metales:
                metales[n2]-=1
                if metales[n2]==0:
                    del metales[n2]
            else:
                ns.append(n2)                    
        ns.remove(n)
    return solve2(ns,a,b,metales)        



def solve():
    [n,a,b] = inputli()
    aux = inputli()
    suma = 0
    metales ={}
    for id,m in enumerate(aux):
        if (m>0):
            suma=max(suma,id+1)
            metales[id+1] = m

    dp = {}
    for i in range(suma,50):
        ans = solve2([i],a,b,metales.copy())
        #print(i,ans,a,b,metales)
        if ans:
            return str(i)
    return "IMPOSSIBLE"



t = inputi()


for i in range(t):

    ans = solve()
    #print("Case #"+str(i+1)+':',print_list(ans),end='')
    print("Case #"+str(i+1)+':',ans,end='')
    print('') if i!=(t-1) else None
