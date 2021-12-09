import math
m,n=map(int,input().split())

while m<=n:
    flag=1
    for i in range(2,math.ceil(m**(1/2))+1):
        if m%i==0:
            flag=0
            break
    if flag:
        print(m)
    m+=1
