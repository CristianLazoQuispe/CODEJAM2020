import sys
from operator import add,sub,itemgetter
import math
import random
 

TOTAL_N = 10000
PEOPLE_N = 100


def sigmoid(gamma):
    if gamma < 0:
        return 1 - 1 / (1 + math.exp(gamma))
    return 1 / (1 + math.exp(-gamma))

def get_cheater(matriz,S_p,Q_p):
    scores = []
    for i in range(PEOPLE_N):
        f=list(map(lambda x:sigmoid(S_p[i]/TOTAL_N-x/PEOPLE_N)>0.5 if random.randint(0, 1)==0 else 1 ,Q_p))
        score = sum(1 for x,y in zip(f,matriz[i]) if x == y) / len(f)
        scores.append(score)
    index, element = max(enumerate(scores), key=itemgetter(1))

    return 1+index

T = int(input())
P = int(input())

for j in range(T):
    matriz1 = []
    matriz = []
    
    #'''
    S_p = []
    Q_p = None
    for i in range(PEOPLE_N):
        texto = sys.stdin.readline().strip()
        lista = list(map(int,list(texto)))
        matriz.append(lista)
        if Q_p is None:
            Q_p = lista
        else:
            Q_p =  list(map(add, Q_p, lista))
        S_p.append(sum(lista))
    
    if random.randint(0, 1)==1:#j<(P*T/100+1):
        ans = get_cheater(matriz,S_p,Q_p)
    else:
        ans = random.randint(1,PEOPLE_N)

    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            