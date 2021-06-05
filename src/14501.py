N=int(input())
T=[0 for _ in range(20)]
P=[0 for _ in range(20)]
dp=[0 for _ in range(20)]
for i in range(N):
    T[i],P[i]=map(int,input().split())

for i in range(N):
    dp[i+1]=max(dp[i],dp[i+1])
    dp[i+T[i]]=max(dp[i+T[i]], dp[i]+P[i])


print(dp[N])

