# Prime time
# Sample ok
# Test case 1 ok 
# Test case 2 Time Limit
# Test case 3 None

import itertools
from functools import reduce


T = int(input())


for j in range(T):

    n = int(input())
    numbers = []
    for i in range(n):
        lista = list(map(int,input().split()))
        numbers+= [lista[0]]*lista[1]
    
    l =numbers
    flags = [False] * len(l)
    ans= 0
    while True:
        a = [l[i] for i, flag in enumerate(flags) if flag]
        b = [l[i] for i, flag in enumerate(flags) if not flag]
        if len(a)!=0 and len(b)!=0:
            suma = sum(a)
            if (suma==reduce((lambda x, y: x * y), b)):
                ans = max(ans,suma)
                #print(a,b)
                #break
        for i in range(len(l)):
            flags[i] = not flags[i]
            if flags[i]:
                break
        else:
            break

    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            
