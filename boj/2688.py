T=int(input())
dp=[list([] for col in range(10)) for row in range(66)]
for i in range(66):
    for j in range(10):
        dp[i][j]=0
for i in range(10):
    dp[1][i]=1
for i in range(2,66):
    for j in range(10):
        for k in range(j,10):
            dp[i][j]+=dp[i-1][k]
for _ in range(T):
    n=int(input())
    print(dp[n+1][0])
