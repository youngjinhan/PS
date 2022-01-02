answer=0
visited=[]

def solution(k, dungeons):
    global N,visited
    N=len(dungeons)
    visited=[0]*N
    dfs(k,0,dungeons)
    return answer

def dfs(k,cnt,dungeons):
    global answer,N,visited
    if cnt>answer:
        answer=cnt
    for i in range(N):
        if k>=dungeons[i][0] and not visited[i]:
            visited[i]=1
            dfs(k-dungeons[i][1], cnt+1, dungeons)
            visited[i]=0
