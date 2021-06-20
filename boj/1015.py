N=int(input())
A=list(map(int,input().split()))
P=[0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if A[i]>A[j]:
            P[i]+=1
        elif A[i]==A[j] and i>j:
            P[i]+=1
            
for i in P:
    print(i, end=' ')
