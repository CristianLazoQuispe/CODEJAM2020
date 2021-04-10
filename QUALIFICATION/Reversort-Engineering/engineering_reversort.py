# sample test : ok
# test 1 : ok
# test 2 : ok

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


def get_reversort(N,C,reference):
    #print('init ',N,C,reference)
    if N==1:
        return [reference+1]
    ans = 'IMPOSSIBLE'
    for i in range(1,N+1):
        n = N-1
        min_c = (n)-1
        max_c = (n*(n+1))/2-1
        #print(i,C-i,max_c,min_c)
        if (C-i)<=max_c and (C-i)>=min_c:
            #print('**',i,N,C,i+reference)
            ans=[i+reference]+get_reversort(N-1,C-i,reference+1)
            break
    return ans
def transform(N,ans):
    # get list 
    aux = [i for i in range(1,N+1)]
    for i in range(N):
        aux[(N-i-1):ans[N-i-1]] = aux[(N-i-1):ans[N-i-1]][::-1]
    # get string for output
    texto = ""
    for i in range(N):
        texto+=str(aux[i])+" "
    return texto[:-1]
for j in range(T):
    lista = list(map(int,input().split()))
    N = int(lista[0])
    C = int(lista[1])
    
    ans = get_reversort(N,C,0)
    
    if ans!= 'IMPOSSIBLE':
        ans = transform(N,ans)
    if j != (T-1):        
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            
