# 1이 출력되는 개수는 피보나치수와 같고, 0이 출력되는 개수는 n-1의 피보나치수와 같음에 착안.

fibo=[0 for _ in range(42)]
fibo[1]=1
fibo[-1]=1  # n=0일때 n-1의 피보나치 값을 1로 고정
for i in range(2,41):
    fibo[i]=fibo[i-1]+fibo[i-2]
T=int(input())
for i in range(T):
    n=int(input())
    print(fibo[n-1],fibo[n])
