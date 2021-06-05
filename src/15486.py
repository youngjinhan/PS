N=int(input())
T=P=dp=[]
T=[0 for _ in range(N+2)]
P=[0 for _ in range(N+2)]
dp=[0 for _ in range(N+2)]

for i in range(N):
    T[i],P[i]=map(int,input().split())

for i in range(N):
    dp[i+1]=max(dp[i],dp[i+1])
    if i+T[i]>N:
        continue
    else:
        dp[i+T[i]]=max(dp[i+T[i]], dp[i]+P[i])


print(dp[N])
