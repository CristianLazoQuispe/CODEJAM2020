# python3
# sample test: ok
# test 1: ok
# test 2: ok

T = int(input())


for j in range(T):
    lista = list(map(str,input().split()))
    x = int(lista[0])
    y = int(lista[1])
    texto = lista[2]
    
    back = None
    ans = 0
    for i in range(len(texto)):
        if texto[i] != "?":
            if back != None:
                if back != texto[i]:
                    if back == 'C':
                        ans+=x
                    else:
                        ans+=y
            back = texto[i]


        #print(texto[:(i+1)],ans,back)
    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')
            
            
