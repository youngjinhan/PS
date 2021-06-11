N,M=map(int,input().split())
castle=[list(input()) for _ in range(N)]
n=[]
m=[]

for i in range(N):
    for j in range(M):
        if castle[i][j]=='X':
            if i not in n:
                n.append(i)
            if j not in m:
                m.append(j)

N-=len(n)
M-=len(m)
print(N) if N>M else print(M)
