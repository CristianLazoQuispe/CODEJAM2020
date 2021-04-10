# Problem Append Sort
# Sample ok
# Test 1 ok
# Test 2 ok
T = int(input())
import math


def get_value(number1,number2):
    cost = 0

    if number1 == number2:
        number2 = number2*10
        cost=1
    elif number2>number1:
        cost=0
    else:
        digit1 = int(math.log10(number1))
        digit2 = int(math.log10(number2))

        if  digit1 == digit2:
            cost+=1
            number2 = number2*10
        else:
            list1 = [int(i) for i in str(number1)]
            list2 = [int(i) for i in str(number2)]
            list2 += [None for i in range(digit1-digit2)]

            for idx,digit in enumerate(list1):
                if list2[idx] ==None:
                    number1_aux = int(''.join(map(str,list1[idx:])))
                    dig_number1_aux = int(math.log10(number1_aux+1))+1
                    if dig_number1_aux>(len(list1)-idx):
                        for i in range(len(list2)):
                            if list2[i] == None:
                                list2[i]=0
                                cost+=1
                        cost+=1
                        list2.append(0)  
                        break
                    else:
                        contador = 1
                        for element in str(number1_aux+1)[::-1]:
                            list2[len(list2)-contador]=int(element)
                            contador+=1
                            cost+=1
                        for i in range(len(list2)):
                            if list2[i] == None:
                                list2[i]=0
                                cost+=1
                        break
                else:
                    if list2[idx]!=digit:
                        for i in range(len(list2)):
                            if list2[i] == None:
                                list2[i]=0
                                cost+=1
                        if list2[idx]<digit:
                             cost+=1
                             list2.append(0)                          
                        break

            number1 = int(''.join(map(str,list1)))
            number2 = int(''.join(map(str,list2)))
            if number1 == number2:
                cost+=1
                number2*=10
    #print('?',number1,number2,cost)
    return cost,number2


for j in range(T):

    n = int(input())
    lista = list(map(int,input().split()))
    back = lista[0]
    ans = 0
    for number in lista[1:]:
        cost,number= get_value(back,number)
        ans+=cost
        back=number

    if j != (T-1):
        print("Case #"+str(j+1)+": "+str(ans))
    else:
        print("Case #"+str(j+1)+": "+str(ans), end='')