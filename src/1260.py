N,M,V=map(int,input().split())
E=[[0 for col in range(N+1)] for row in range(N+1)]
for _ in range(M):
    i,j=map(int,input().split())
    E[i][j]=E[j][i]=1

dfs=[V]
cur=V
i=0
while i<=N:
    if E[cur][i]==1 and i not in dfs:
        dfs.append(i)
        j=i
        cur=j
        i=-1
    i+=1
    if i>N:
        if len(dfs)==N:
            break
        else:
            if dfs.index(cur)==0:
                break
            else:
                cur=dfs[dfs.index(cur)-1]
                i=0
            
print(*dfs)

q=[V]
bfs=[V]
while q:
    for i in range(N+1):
        if E[q[0]][i]==1 and i not in bfs:
            q.append(i)
            bfs.append(i)
    del q[0]
print(*bfs)
    
