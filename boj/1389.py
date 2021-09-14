import sys
from collections import deque

def bfs(x):
    q = deque()
    q.append((x, 0))
    total = 0

    while q:
        s, d = q.popleft()
        total += d
        for i in arr[s]:
            if not visited[i]:
                visited[i] = True
                q.append((i, d + 1))

    return total


input = sys.stdin.readline
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
arr = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer = []

for i, j in relations:
    arr[i].append(j)
    arr[j].append(i)

for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    answer.append(bfs(i))

print(answer.index(min(answer)) + 1)
