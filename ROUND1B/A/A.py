import itertools
import math

def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))

m = 1000000007
back = 15709090909091
mod = 12*60*60*(10**9)
tick = (1/12)*(10**(-10))


def print_list(lista):
    s=""
    for i in lista[:-1]:
        s+=str(i)+" "
    s+=str(lista[-1])

    return s

def tmr(a,b,c):
    t = (((b-a)*back)%mod +mod )%mod
    if((708*t -c +b)%mod ==0):
        n = int(t%(10**9))
        t/=(10**9)
        s = math.floor(t%60)
        t /=60
        m = math.floor(t%60)
        h = math.floor(t/60)
        return True,[h,m,s,n]
    return False,[-8,-8,-8]
def process(h_g,m_g,s_g):
    #print("tick ",h_t,m_t,s_t)
    #h_g = h_t*tick
    #m_g = m_t*(tick)
    #s_g = s_t*(tick)
    
    h = math.floor(h_g/30)
    m_aprox = (h_g-h*30)*12

    if abs(m_aprox - m_g)<= 120*tick:    
        m = math.floor(m_g/6)
        s_aprox = (m_g-m*6)*60
        if abs(s_aprox-s_g)<= 720*tick:    
            s = math.floor(s_g/6)
            n_aprox = (s_g-s*6)*(10**8)
            n_aprox = math.ceil(n_aprox)
            #print(h,m,s,n_aprox)
            return True,[h,m,s,n_aprox]

    return False,[-5,-5,-5]

def process2(h_t,m_t,s_t):

    return tmr(h_t,m_t,s_t)

    h_g1 = h_t*tick
    m_g1 = m_t*tick
    s_g1 = s_t*tick
    
    #print(h_g,m_g,s_g)

    rotate = 0
    while(rotate<360):
        h_g = (h_g1-rotate)
        if h_g<0:
            h_g+=360
        m_g = (m_g1-rotate)
        if m_g<0:
            m_g+=360
        s_g = (s_g1-rotate)
        if s_g<0:
            s_g+=360
        ban,ans = process(h_g,m_g,s_g)
        if ban:
            return True,ans
        rotate+=1


    return False,[-6,-6,-6]
def solve():
    [a,b,c] = inputli()
    
    for [h,m,s] in list(itertools.permutations([a,b,c])):
        ban,ans = process2(h,m,s)
        if ban ==True:
            return ans
    return [0,0,0]
t = inputi()


for i in range(t):

    ans = solve()
    #print("ans ",ans)
    print("Case #"+str(i+1)+':',print_list(ans),end='')
    #print("Case #"+str(i+1)+':',ans,end='')
    print('') if i!=(t-1) else None
