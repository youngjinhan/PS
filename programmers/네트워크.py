# 내 풀이
check=[]
def connect(node,n,computers):
    check.append(node)
    
    for i in range(n):
        if computers[node][i]==1 and i not in check:
            connect(i,n,computers)

def solution(n, computers):
    answer = 0
    for i in range(n):
        if i not in check:
            connect(i,n,computers)
            answer+=1
        
    return answer


# 인터넷 검색한 풀이
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
