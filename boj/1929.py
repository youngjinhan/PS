# 방법 1
import math
m,n=map(int,input().split(' '))

while m<=n:
    flag=1
    for i in range(2,math.ceil(m**(1/2))+1):
        if m%i==0:
            flag=0
            break
    if m==1:
        m+=1
        continue
    if flag or m==2:
        print(m)
    m+=1

# 방법 2
m,n=map(int,input().split())

# 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
sieve = [True] * (n+1)
sieve[1]=False

# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
o = int(n ** 0.5)
for i in range(2, o + 1):
    if sieve[i] == True:           # i가 소수인 경우
        for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
            sieve[j] = False

for i in range(m,n+1):
    if sieve[i]==True:
        print(i)
